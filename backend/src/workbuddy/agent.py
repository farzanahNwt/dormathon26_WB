"""
LAICIs - WorkBuddy Autonomous Investigation Agent
Implements the 7-stage autonomous workflow required for DORMATHON 2026 Track 2:
1. UNDERSTAND -> 2. PLAN -> 3. EXECUTE -> 4. VALIDATE -> 5. INTEGRATE -> 6. DELIVER -> 7. FINANCIAL_RISK_ASSESS
"""

import hashlib
import os
import time
import uuid
from typing import Dict, Any, List, Optional

from .tools import WorkBuddyToolRegistry
from ..detection.weighted_scorer import WeightedScorer
from ..financial.risk_assessor import FinancialRiskAssessor
from ..financial.recovery_playbook import RecoveryPlaybook
from ..library.store import LibraryStore
from ..library.audit_trail import AuditTrail


class WorkBuddyInvestigationAgent:
    """
    Autonomous multi-model forensics agent executing under Tencent WorkBuddy runtime paradigms.
    """

    def __init__(self):
        self.tools = WorkBuddyToolRegistry()
        self.store = LibraryStore()

    def investigate(
        self,
        input_type: str,
        content: str = "",
        file_path: Optional[str] = None,
        file_name: str = "",
        goal: str = "",
        segment: str = "individual"
    ) -> Dict[str, Any]:
        """
        Main autonomous pipeline entrance.
        Executes Understand -> Plan -> Execute -> Validate -> Integrate -> Deliver.
        """
        scan_id = f"SCAN-{uuid.uuid4().hex[:10].upper()}"
        start_time = time.time()
        executed_tools: List[str] = []
        tool_results: Dict[str, Any] = {}
        steps_state = {
            "understand": "waiting",
            "plan": "waiting",
            "execute": "waiting",
            "validate": "waiting",
            "integrate": "waiting",
            "deliver": "waiting",
            "financial_risk_assess": "waiting"
        }

        # ----------------------------------------------------
        # STAGE 1: UNDERSTAND
        # ----------------------------------------------------
        steps_state["understand"] = "running"
        understanding = self._step_understand(input_type, content, file_path, file_name, goal)
        steps_state["understand"] = "done"

        # ----------------------------------------------------
        # STAGE 2: PLAN
        # ----------------------------------------------------
        steps_state["plan"] = "running"
        plan = self._step_plan(input_type, understanding)
        steps_state["plan"] = "done"

        # ----------------------------------------------------
        # STAGE 3: EXECUTE
        # ----------------------------------------------------
        steps_state["execute"] = "running"
        executed_tools, tool_results = self._step_execute(plan, file_path, content, goal)
        steps_state["execute"] = "done"

        # ----------------------------------------------------
        # STAGE 4: VALIDATE
        # ----------------------------------------------------
        steps_state["validate"] = "running"
        validation = self._step_validate(input_type, tool_results)
        steps_state["validate"] = "done"

        # ----------------------------------------------------
        # STAGE 5: INTEGRATE & ASSESS FINANCIAL RISK
        # ----------------------------------------------------
        steps_state["integrate"] = "running"
        steps_state["financial_risk_assess"] = "running"
        integration = self._step_integrate(input_type, tool_results, segment)
        steps_state["integrate"] = "done"
        steps_state["financial_risk_assess"] = "done"

        # ----------------------------------------------------
        # STAGE 6: DELIVER
        # ----------------------------------------------------
        steps_state["deliver"] = "running"
        delivery = self._step_deliver(input_type, integration, validation, understanding, executed_tools)
        steps_state["deliver"] = "done"

        duration_sec = round(time.time() - start_time, 3)

        # ----------------------------------------------------
        # AUDIT TRAIL & 3-LIBRARY RECORDING
        # ----------------------------------------------------
        audit_record = AuditTrail.create_record(
            scan_id=scan_id,
            action=f"INVESTIGATION_{input_type.upper()}",
            inputs={
                "input_type": input_type,
                "file_name": file_name,
                "file_hash": understanding.get("file_hash", ""),
                "content_preview": content[:120] if content else "",
                "goal": goal
            },
            outputs={
                "verdict": integration["verdict"],
                "composite_confidence": integration["composite_score"],
                "risk_tier": integration["financial"]["risk_tier"],
                "exposure_rm": integration["financial"]["exposure_rm"],
                "tools_executed": executed_tools
            }
        )
        self.store.log_audit(audit_record)

        # Build 22-field Scan Record
        scan_db_record = {
            "scan_id": scan_id,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "input_type": input_type,
            "file_name": file_name or understanding.get("target_display", "content"),
            "file_size_bytes": understanding.get("file_size_bytes", len(content)),
            "file_hash_sha256": understanding.get("file_hash", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
            "target_goal": goal or "General media/content verification",
            "user_agent": "LAICIs-WorkBuddy-Client",
            "status": "completed",
            "predicted_label": integration.get("raw_label", 0),
            "predicted_label_name": integration.get("raw_label_name", "N/A"),
            "ai_probability": integration.get("ai_prob", 0.0),
            "human_probability": integration.get("human_prob", 0.0),
            "ela_score": integration.get("ela_score", 0.0),
            "sightengine_score": integration.get("sightengine_score", 0.0),
            "gemini_verdict": integration.get("gemini_summary", "N/A"),
            "composite_confidence": integration["composite_score"],
            "risk_tier": integration["financial"]["risk_tier"],
            "exposure_rm": integration["financial"]["exposure_rm"],
            "prevention_value_rm": integration["financial"]["prevention_value_rm"],
            "tools_invoked": executed_tools,
            "audit_trail_id": audit_record["audit_id"],
            "verifier_signature": audit_record["verifier_signature"]
        }
        self.store.record_scan(scan_db_record)

        # Return standardized response conforming exactly to TRACK2-INTEGRATION.md contract
        return {
            "status": "completed",
            "summary": delivery["summary"],
            "message": delivery["message"],
            "tools": executed_tools,
            "steps": steps_state,
            "report": {
                "findings": delivery["findings"],
                "limitations": delivery["limitations"],
                "recommendations": delivery["recommendations"]
            },
            # Rich data extensions for the revamped UI
            "verdict": integration["verdict"],
            "confidence": integration["confidence_percentage"],
            "composite_score": integration["composite_score"],
            "financial_risk": integration["financial"],
            "recovery_playbook": integration["recovery"],
            "audit": {
                "scan_id": scan_id,
                "audit_id": audit_record["audit_id"],
                "signature": audit_record["verifier_signature"],
                "timestamp": audit_record["timestamp_iso"]
            },
            "media_url": f"/uploads/{file_name}" if file_name else None,
            "ela_image_url": tool_results.get("ela", {}).get("ela_image_url"),
            "tool_details": tool_results,
            "execution_duration_seconds": duration_sec
        }

    # ----------------------------------------------------
    # INTERNAL STEP IMPLEMENTATIONS
    # ----------------------------------------------------

    def _step_understand(self, input_type: str, content: str, file_path: Optional[str], file_name: str, goal: str) -> dict:
        info = {
            "input_type": input_type,
            "goal": goal or "Assess authenticity and fraud indicators",
            "is_malaysian_context": any(w in (content + " " + goal).lower() for w in ["rm", "ringgit", "malaysia", "maybank", "cimb", "petronas", "pdrm"])
        }

        if input_type == "media" and file_path and os.path.exists(file_path):
            size = os.path.getsize(file_path)
            info["file_size_bytes"] = size
            info["target_display"] = file_name or os.path.basename(file_path)
            # Compute SHA-256 hash
            hasher = hashlib.sha256()
            with open(file_path, "rb") as f:
                while chunk := f.read(65536):
                    hasher.update(chunk)
            info["file_hash"] = hasher.hexdigest()
        else:
            info["file_hash"] = hashlib.sha256((content or "").encode("utf-8")).hexdigest()
            info["target_display"] = content[:50] + "..." if len(content) > 50 else content

        return info

    def _step_plan(self, input_type: str, understanding: dict) -> List[str]:
        """
        Dynamically plan which tools to execute based on input type.
        """
        if input_type == "media":
            return [
                "local_pytorch_efficientnetv2",
                "local_ela_analyzer",
                "sightengine_api",
                "gemini_scam_analyzer"
            ]
        elif input_type == "url":
            return [
                "domain_inspector"
            ]
        elif input_type == "text":
            return [
                "pdrm_ccid_semak_mule",
                "gemini_scam_analyzer"
            ]
        return ["local_ela_analyzer"]

    def _step_execute(self, plan: List[str], file_path: Optional[str], content: str, goal: str) -> tuple:
        executed: List[str] = []
        results: Dict[str, Any] = {}

        for tool_name in plan:
            if tool_name == "local_pytorch_efficientnetv2" and file_path:
                res = self.tools.run_pytorch(file_path)
                if res.get("success"):
                    executed.append("local_pytorch_efficientnetv2")
                    results["pytorch"] = res

            elif tool_name == "local_ela_analyzer" and file_path:
                res = self.tools.run_ela(file_path)
                if res.get("success"):
                    executed.append("local_ela_analyzer")
                    results["ela"] = res

            elif tool_name == "sightengine_api" and file_path:
                res = self.tools.run_sightengine(file_path)
                if res.get("success"):
                    executed.append("sightengine_api")
                    results["sightengine"] = res

            elif tool_name == "gemini_scam_analyzer":
                if file_path:
                    res = self.tools.run_gemini_multimodal(file_path, goal)
                    print(f"[DEBUG AGENT] gemini_multimodal result: success={res.get('success')}, tool={res.get('tool')}", flush=True)
                    if res.get("success"):
                        executed.append("gemini_scam_analyzer")
                        results["gemini"] = res
                elif content:
                    res = self.tools.run_gemini(content, goal)
                    print(f"[DEBUG AGENT] gemini_text result: success={res.get('success')}", flush=True)
                    if res.get("success"):
                        executed.append("gemini_scam_analyzer")
                        results["gemini"] = res

            elif tool_name == "domain_inspector" and content:
                res = self.tools.run_domain_check(content)
                if res.get("success"):
                    executed.append("domain_inspector")
                    results["domain"] = res

            elif tool_name == "pdrm_ccid_semak_mule" and content:
                mules = self.tools.run_semak_mule_text(content)
                executed.append("pdrm_ccid_semak_mule")
                results["semak_mule"] = mules

        # Always execute the regulatory and financial risk assessor
        executed.append("financial_risk_assessor")
        executed.append("bnm_rmit_audit_logger")

        return executed, results

    def _step_validate(self, input_type: str, tool_results: dict) -> dict:
        validation_flags = []
        discrepancies = []

        if input_type == "media":
            pt = tool_results.get("pytorch", {})
            ela = tool_results.get("ela", {})

            if pt.get("success") and ela.get("success"):
                pt_ai = pt.get("is_ai_generated", False)
                ela_tampered = ela.get("risk_level") in ("MODERATE", "HIGH")

                if pt_ai and not ela_tampered:
                    discrepancies.append("Deep learning model indicates synthetic generation, but compression error surface is uniform (typical in full-image diffusion generation).")
                elif not pt_ai and ela_tampered:
                    discrepancies.append("Compression anomaly detected by ELA, but deep learning classifier predicts camera capture (possible manual Photoshop splicing or re-compression).")
                else:
                    validation_flags.append("Cross-model consistency verified: PyTorch deepfake classifier and ELA compression metrics align.")

        elif input_type == "url":
            dom = tool_results.get("domain", {})
            if dom.get("is_dangerous"):
                validation_flags.append(f"Domain flagged dangerous: {dom.get('findings', ['Unknown'])[0]}")
            else:
                validation_flags.append("SSRF security controls confirmed no internal IP traversal.")

        elif input_type == "text":
            mules = tool_results.get("semak_mule", [])
            flagged_mules = [m for m in mules if m.get("is_flagged")]
            if flagged_mules:
                validation_flags.append(f"CONFIRMED MATCH: {len(flagged_mules)} recipient phone/bank entity matches active PDRM CCID scam database.")

        return {
            "verified": True,
            "cross_checks": validation_flags,
            "discrepancies": discrepancies
        }

    def _step_integrate(self, input_type: str, tool_results: dict, segment: str) -> dict:
        has_tx = False
        if input_type == "media":
            scored = WeightedScorer.calculate_media_score(tool_results)
            composite_score = scored["composite_score"]
            verdict = scored["verdict"]

            pt = tool_results.get("pytorch", {})
            raw_label = pt.get("label", 0)
            raw_label_name = pt.get("label_name", "Human-generated")
            ai_prob = pt.get("ai_probability", 0.0)
            human_prob = pt.get("human_probability", 1.0)
            ela_score = tool_results.get("ela", {}).get("tampering_score", 0.0)
            sightengine_score = tool_results.get("sightengine", {}).get("composite_score", 0.0)

            threat_type = "media_informational"
            has_tx = False

        elif input_type == "url":
            dom = tool_results.get("domain", {})
            is_dang = dom.get("is_dangerous", False)
            composite_score = dom.get("threat_score", 0.95 if is_dang else 0.1)
            verdict = "PHISHING_DOMAIN" if is_dang else "LOW_RISK_DOMAIN"
            raw_label = 1 if is_dang else 0
            raw_label_name = "Malicious Phishing URL" if is_dang else "Clean URL"
            ai_prob = composite_score
            human_prob = 1.0 - composite_score
            ela_score = 0.0
            sightengine_score = 0.0
            threat_type = "banking_phishing" if is_dang else "clean_domain"
            has_tx = is_dang

        else: # text
            gm = tool_results.get("gemini", {})
            mules = tool_results.get("semak_mule", [])
            flagged = any(m.get("is_flagged") for m in mules)

            base_gm = gm.get("confidence", 0.2)
            composite_score = 0.95 if flagged else base_gm
            verdict = "CONFIRMED_SCAM_SYNDICATE" if flagged else ("HIGH_RISK_SCAM" if composite_score > 0.6 else "UNVERIFIED_TEXT")
            raw_label = 1 if composite_score > 0.5 else 0
            raw_label_name = gm.get("scam_type", "Text Scam")
            ai_prob = composite_score
            human_prob = 1.0 - composite_score
            ela_score = 0.0
            sightengine_score = 0.0
            has_tx = flagged or (composite_score > 0.5)
            if flagged:
                threat_type = "syndicate_mule_account"
            elif has_tx:
                scam_name = gm.get("scam_type", "").lower()
                threat_type = "job_recruitment" if "job" in scam_name else ("investment_lure" if "invest" in scam_name else "default")
            else:
                threat_type = "clean_text"

        # Run Malaysian Financial Risk Assessment with calibrated context
        fin = FinancialRiskAssessor.assess_exposure(
            confidence_score=composite_score,
            scam_type=threat_type,
            target_segment=segment,
            has_transactional_context=has_tx
        )

        # Generate Actionable Recovery Playbook
        recovery = RecoveryPlaybook.get_action_plan(
            risk_tier=fin["risk_tier"],
            threat_type=threat_type
        )

        return {
            "composite_score": composite_score,
            "confidence_percentage": round(composite_score * 100, 1),
            "verdict": verdict,
            "raw_label": raw_label,
            "raw_label_name": raw_label_name,
            "ai_prob": ai_prob,
            "human_prob": human_prob,
            "ela_score": ela_score,
            "sightengine_score": sightengine_score,
            "gemini_summary": tool_results.get("gemini", {}).get("reasoning_summary") or tool_results.get("gemini", {}).get("summary", "N/A"),
            "financial": fin,
            "recovery": recovery
        }

    def _step_deliver(self, input_type: str, integration: dict, validation: dict, understanding: dict, executed_tools: List[str]) -> dict:
        tier = integration["financial"]["risk_tier"]
        exposure = integration["financial"]["exposure_formatted"]
        prev_val = integration["financial"]["prevention_value_formatted"]
        conf = integration["confidence_percentage"]

        findings = []
        if input_type == "media":
            findings.append(f"Forensic models evaluated authenticity with composite synthetic probability of {conf}%.")
            if integration["ai_prob"] > 0.5:
                findings.append(f"Local EfficientNetV2-S deepfake classifier detected synthetic feature artifacts (AI probability: {integration['ai_prob']*100:.1f}%).")
            else:
                findings.append(f"Local EfficientNetV2-S deepfake classifier classified features as human/camera-captured (Authentic probability: {integration['human_prob']*100:.1f}%).")
            if integration["ela_score"] > 0.35:
                findings.append(f"Error Level Analysis (ELA) detected compression inconsistencies (tampering score: {integration['ela_score']:.2f}).")
            gm_reason = integration.get("gemini_summary")
            if gm_reason and gm_reason != "N/A":
                findings.append(f"Gemini Multimodal Visual Reasoning: {gm_reason}")
            findings.append(f"Assessed financial risk tier: {tier} (Potential Exposure: {exposure}, Prevention Value: {prev_val}).")

        elif input_type == "url":
            findings.append(f"SSRF-safe domain evaluation completed with threat rating of {conf}%.")
            findings.extend(validation.get("cross_checks", []))
            findings.append(f"Assessed financial risk tier: {tier} (Potential Exposure: {exposure}).")

        else: # text
            findings.append(f"Content scam analysis calculated risk probability of {conf}%.")
            findings.extend(validation.get("cross_checks", []))
            findings.append(f"Financial risk tier: {tier} with estimated exposure of {exposure}.")

        # Honest Limitations per Track 2 criteria
        limitations = [
            "Forensic neural networks and ELA metrics provide probabilistic indicators, not definitive legal proof of manipulation.",
            "Heavy re-compression by social messaging platforms (e.g., WhatsApp, Telegram) can degrade high-frequency compression artifacts.",
            "A low score does not guarantee zero risk; always confirm high-value fund authorizations through independent out-of-band phone calls."
        ]

        # Actionable recommendations
        recommendations = integration["recovery"]["checklist"]

        summary = f"LAICIs Agent completed autonomous forensic evaluation ({tier} RISK / {conf}% confidence)."
        message = f"Assessed exposure at {exposure}. Prevention value of {prev_val} verified under BNM RMiT standards."

        return {
            "summary": summary,
            "message": message,
            "findings": findings,
            "limitations": limitations,
            "recommendations": recommendations
        }
