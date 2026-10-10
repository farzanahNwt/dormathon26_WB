"""
LAICIs - Sightengine Visual AI Client
Performs deepfake and generative AI visual screening via Sightengine API.
Gracefully handles quota limits, connection timeouts, and offline states.
"""

import os
import requests


class SightengineClient:
    """
    Sightengine API client for AI-generated media and deepfake detection.
    """

    def __init__(self, api_user: str = None, api_secret: str = None):
        self.api_user = api_user or os.environ.get("SIGHTENGINE_API_USER", "")
        self.api_secret = api_secret or os.environ.get("SIGHTENGINE_API_SECRET", "")
        self.api_secret_alt = os.environ.get("SIGHTENGINE_API_SECRET_ALT", "")
        self.endpoint = "https://api.sightengine.com/1.0/check.json"

    def analyze_image(self, image_path: str) -> dict:
        """
        Check image with Sightengine for GenAI/Deepfake indicators.
        """
        if not os.path.exists(image_path):
            return {"success": False, "error": f"File not found: {image_path}"}

        credentials_to_try = [
            (self.api_user, self.api_secret),
            (self.api_user, self.api_secret_alt)
        ]

        last_error = "Sightengine API failure"
        for user, secret in credentials_to_try:
            params = {
                "models": "genai,deepfake",
                "api_user": user,
                "api_secret": secret
            }

            try:
                with open(image_path, "rb") as f:
                    files = {"media": f}
                    response = requests.post(self.endpoint, files=files, data=params, timeout=12)

                if response.status_code == 200:
                    data = response.json()
                    if data.get("status") == "success":
                        type_data = data.get("type", {})
                        genai_score = float(type_data.get("ai_generated", 0.0))
                        
                        deepfake_data = data.get("deepfake", {})
                        deepfake_score = float(deepfake_data.get("score", 0.0)) if isinstance(deepfake_data, dict) else 0.0

                        max_score = max(genai_score, deepfake_score)
                        
                        return {
                            "success": True,
                            "tool": "sightengine_api",
                            "ai_generated_score": round(genai_score, 4),
                            "deepfake_score": round(deepfake_score, 4),
                            "composite_score": round(max_score, 4),
                            "is_flagged": bool(max_score > 0.5),
                            "raw_response": data
                        }
                    else:
                        last_error = data.get("error", {}).get("message", "API reported failure")
                elif response.status_code in (401, 403):
                    last_error = f"HTTP {response.status_code} authentication error"
                    continue
                else:
                    last_error = f"HTTP status {response.status_code}"
            except Exception as e:
                last_error = str(e)

        return {
            "success": False,
            "tool": "sightengine_api",
            "error": last_error
        }
