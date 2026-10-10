"""
LAICIs - Multi-Model Forensic Scorer
Fuses results from multiple detection tools into an objective weighted composite score.
"""

from typing import Dict, Any


class WeightedScorer:
    """
    Computes normalized multi-model confidence scores based on available tools.
    """

    DEFAULT_MEDIA_WEIGHTS = {
        "local_pytorch_efficientnetv2": 0.40,
        "local_ela_analyzer": 0.25,
        "sightengine_api": 0.20,
        "gemini_analyzer": 0.15
    }

    @staticmethod
    def calculate_media_score(tool_results: Dict[str, Any]) -> Dict[str, Any]:
        weights = {}
        scores = {}

        # 1. PyTorch
        if "pytorch" in tool_results and tool_results["pytorch"].get("success"):
            pt = tool_results["pytorch"]
            scores["local_pytorch_efficientnetv2"] = pt.get("ai_probability", 0.0)
            weights["local_pytorch_efficientnetv2"] = WeightedScorer.DEFAULT_MEDIA_WEIGHTS["local_pytorch_efficientnetv2"]

        # 2. ELA
        if "ela" in tool_results and tool_results["ela"].get("success"):
            ela = tool_results["ela"]
            scores["local_ela_analyzer"] = ela.get("tampering_score", 0.0)
            weights["local_ela_analyzer"] = WeightedScorer.DEFAULT_MEDIA_WEIGHTS["local_ela_analyzer"]

        # 3. Sightengine
        if "sightengine" in tool_results and tool_results["sightengine"].get("success"):
            se = tool_results["sightengine"]
            scores["sightengine_api"] = se.get("composite_score", 0.0)
            weights["sightengine_api"] = WeightedScorer.DEFAULT_MEDIA_WEIGHTS["sightengine_api"]

        # 4. Gemini (Multimodal or Contextual)
        if "gemini" in tool_results and tool_results["gemini"].get("success"):
            gm = tool_results["gemini"]
            if "ai_confidence" in gm:
                scores["gemini_analyzer"] = gm.get("ai_confidence", 0.0)
            else:
                scores["gemini_analyzer"] = gm.get("confidence", 0.0) if gm.get("is_scam") else 0.1
            weights["gemini_analyzer"] = WeightedScorer.DEFAULT_MEDIA_WEIGHTS["gemini_analyzer"]

        if not weights:
            return {
                "composite_score": 0.0,
                "confidence_percentage": 0.0,
                "verdict": "INCONCLUSIVE",
                "explanation": "No verification models executed successfully."
            }

        total_weight = sum(weights.values())
        composite_score = sum(scores[k] * weights[k] for k in weights) / total_weight

        # Classify verdict
        if composite_score >= 0.70:
            verdict = "HIGH_CONFIDENCE_SYNTHETIC"
            desc = "Multiple forensic indicators confirm synthetic generation or digital tampering."
        elif composite_score >= 0.40:
            verdict = "SUSPICIOUS_ANOMALIES"
            desc = "Incongruent compression artifacts or synthetic markers present. Independent verification required."
        else:
            verdict = "CONSISTENT_WITH_AUTHENTIC"
            desc = "Forensic signals are consistent with authentic camera-captured media."

        return {
            "composite_score": round(composite_score, 4),
            "confidence_percentage": round(composite_score * 100, 1),
            "verdict": verdict,
            "description": desc,
            "model_breakdown": {
                k: {"score": round(scores[k], 4), "weight_applied": round(weights[k] / total_weight, 2)}
                for k in scores
            }
        }
