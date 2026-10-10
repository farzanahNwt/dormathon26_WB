"""
LAICIs - Local PyTorch Deepfake & AI Image Classifier
Loads trained EfficientNetV2-S model (best_model.pth) to perform instant local inference.
"""

import os
import sys
import numpy as np
from PIL import Image

# Global model cache to avoid reloading on every request
_MODEL_INSTANCE = None
_DEVICE = None

# Resolve model path across clean backend and legacy layouts
_candidates = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "models", "best_model.pth")),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "best_model.pth")),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "petronascybersec-main", "petronascybersec-main", "best_model.pth")),
]
MODEL_PATH_DEFAULT = next((p for p in _candidates if os.path.exists(p)), _candidates[0])
IMG_SIZE = 384
NUM_CLASSES = 2
MODEL_NAME = "tf_efficientnetv2_s.in21k_ft_in1k"


class PyTorchDetector:
    """
    Local deepfake classifier powered by fine-tuned EfficientNetV2-S.
    """

    def __init__(self, model_path: str = None):
        self.model_path = model_path or MODEL_PATH_DEFAULT
        self.device = None
        self.model = None
        self._ensure_loaded()

    def _ensure_loaded(self):
        global _MODEL_INSTANCE, _DEVICE
        if _MODEL_INSTANCE is not None:
            self.model = _MODEL_INSTANCE
            self.device = _DEVICE
            return

        try:
            import torch
            import timm
            
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            _DEVICE = self.device

            if not os.path.exists(self.model_path):
                print(f"[PyTorchDetector] Model file not found at {self.model_path}", file=sys.stderr)
                return

            model = timm.create_model(MODEL_NAME, pretrained=False, num_classes=NUM_CLASSES)
            state_dict = torch.load(self.model_path, map_location=self.device)
            model.load_state_dict(state_dict)
            model.to(self.device)
            model.eval()

            _MODEL_INSTANCE = model
            self.model = model
            print(f"[PyTorchDetector] Successfully initialized model from {self.model_path} on {self.device}")

        except Exception as e:
            print(f"[PyTorchDetector] Failed to load PyTorch model: {e}", file=sys.stderr)
            self.model = None

    def predict(self, image_path: str) -> dict:
        """
        Run inference on an image file.
        
        Returns:
            dict containing label, label_name, confidence, ai_probability, human_probability
        """
        if not os.path.exists(image_path):
            return {
                "success": False,
                "error": f"Image file not found: {image_path}"
            }

        if self.model is None:
            self._ensure_loaded()
            if self.model is None:
                return {
                    "success": False,
                    "error": "PyTorch model is not initialized or weights missing."
                }

        try:
            import torch
            import albumentations as albu
            from albumentations.pytorch import ToTensorV2

            val_transform = albu.Compose([
                albu.Resize(IMG_SIZE, IMG_SIZE),
                albu.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
                ToTensorV2()
            ])

            ext = os.path.splitext(image_path)[1].lower()
            is_video = ext in ('.mp4', '.avi', '.mov', '.mkv', '.webm')

            images_to_process = []
            if is_video:
                import cv2
                cap = cv2.VideoCapture(image_path)
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                if total_frames > 0:
                    indices = np.linspace(0, total_frames - 1, min(5, total_frames), dtype=int)
                    for idx in indices:
                        cap.set(cv2.CAP_PROP_POS_FRAMES, int(idx))
                        ret, frame = cap.read()
                        if ret:
                            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            images_to_process.append(Image.fromarray(rgb))
                cap.release()
                if not images_to_process:
                    return {"success": False, "error": "Unable to decode frames from video."}
            else:
                image = Image.open(image_path)
                if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                    image = image.convert('RGBA')
                images_to_process.append(image.convert("RGB"))

            frame_results = []
            with torch.no_grad():
                for img in images_to_process:
                    image_np = np.array(img)
                    transformed = val_transform(image=image_np)
                    input_tensor = transformed["image"].unsqueeze(0).to(self.device)
                    outputs = self.model(input_tensor)
                    probs = torch.nn.functional.softmax(outputs, dim=1)
                    frame_results.append({
                        "human": float(probs[0][0].item()),
                        "ai": float(probs[0][1].item())
                    })

            # Calculate aggregated probabilities across frames
            mean_ai = float(np.mean([f["ai"] for f in frame_results]))
            mean_human = float(np.mean([f["human"] for f in frame_results]))
            peak_ai = float(np.max([f["ai"] for f in frame_results]))

            # Threshold: flag if average > 0.5 or peak frame artifact > 0.70
            predicted_label = 1 if (mean_ai > 0.5 or (is_video and peak_ai > 0.70)) else 0
            confidence = peak_ai if predicted_label == 1 else mean_human

            # Label 0: Human-generated / Authentic, Label 1: AI-generated / Deepfake
            label_name = "AI-generated" if predicted_label == 1 else "Human-generated"

            return {
                "success": True,
                "tool": "local_pytorch_efficientnetv2",
                "model_name": MODEL_NAME,
                "label": predicted_label,
                "label_name": label_name,
                "ai_probability": round(mean_ai, 4),
                "human_probability": round(mean_human, 4),
                "peak_ai_probability": round(peak_ai, 4),
                "confidence": round(confidence, 4),
                "is_ai_generated": bool(predicted_label == 1),
                "is_video": is_video,
                "frames_analyzed": len(images_to_process)
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"Inference execution failed: {str(e)}"
            }
