"""
LAICIs - Local Error Level Analysis (ELA) Analyzer
Detects JPEG compression inconsistencies and digital tampering artifacts.
Operates completely offline with zero API dependencies.
"""

import io
import os
import numpy as np
from PIL import Image, ImageChops, ImageEnhance


class ELAAnalyzer:
    """
    Error Level Analysis (ELA) for image forensic tampering detection.
    Compares original pixel values against recompressed JPEG values to identify
    resaved, manipulated, or spliced regions.
    """

    def __init__(self, default_quality: int = 90, scale_factor: int = 15):
        self.default_quality = default_quality
        self.scale_factor = scale_factor

    def analyze(self, image_path: str, quality: int = None) -> dict:
        """
        Run ELA on an image file.
        
        Args:
            image_path: Path to the image file
            quality: JPEG quality level (default 90)
            
        Returns:
            dict containing ELA metrics, risk tier, and forensic observations
        """
        if quality is None:
            quality = self.default_quality

        if not os.path.exists(image_path):
            return {
                "success": False,
                "error": f"Image file not found: {image_path}"
            }

        try:
            # 1. Open original image or extract middle keyframe if video
            ext = os.path.splitext(image_path)[1].lower()
            is_video = ext in ('.mp4', '.avi', '.mov', '.mkv', '.webm')

            if is_video:
                import cv2
                cap = cv2.VideoCapture(image_path)
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                original = None
                if total_frames > 0:
                    mid_frame = total_frames // 2
                    cap.set(cv2.CAP_PROP_POS_FRAMES, mid_frame)
                    ret, frame = cap.read()
                    if ret:
                        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        original = Image.fromarray(rgb)
                cap.release()
                if original is None:
                    return {"success": False, "error": "Could not extract video keyframe for ELA"}
            else:
                original = Image.open(image_path)
                if original.mode in ('RGBA', 'LA') or (original.mode == 'P' and 'transparency' in original.info):
                    original = original.convert('RGBA')
                original = original.convert("RGB")

            orig_array = np.array(original, dtype=np.float32)

            # 2. Resave to in-memory JPEG at specified quality
            buffer = io.BytesIO()
            original.save(buffer, format="JPEG", quality=quality)
            buffer.seek(0)
            resaved = Image.open(buffer).convert("RGB")
            resaved_array = np.array(resaved, dtype=np.float32)

            # 3. Calculate absolute difference
            diff_array = np.abs(orig_array - resaved_array)
            mean_diff = float(np.mean(diff_array))
            max_diff = float(np.max(diff_array))
            std_diff = float(np.std(diff_array))

            # 4. Generate visual ELA map (scaled difference)
            scaled_diff = np.clip(diff_array * self.scale_factor, 0, 255).astype(np.uint8)
            ela_image = Image.fromarray(scaled_diff)

            # Save visual ELA map to uploads directory
            base_filename = os.path.basename(image_path)
            clean_name = os.path.splitext(base_filename)[0]
            ela_filename = f"ela_{clean_name}.jpg"
            ela_disk_path = os.path.join(os.path.dirname(image_path), ela_filename)
            ela_image_url = None
            try:
                ela_image.save(ela_disk_path, format="JPEG", quality=90)
                ela_image_url = f"/uploads/{ela_filename}"
            except Exception:
                ela_image_url = None

            # 5. Grid patch variance analysis (detect localized tampering)
            h, w, _ = diff_array.shape
            grid_size = 16
            patch_means = []
            
            for y in range(0, h - grid_size, grid_size):
                for x in range(0, w - grid_size, grid_size):
                    patch = diff_array[y:y+grid_size, x:x+grid_size]
                    patch_means.append(np.mean(patch))

            if patch_means:
                patch_variance = float(np.var(patch_means))
                patch_max_mean = float(np.max(patch_means))
            else:
                patch_variance = 0.0
                patch_max_mean = mean_diff

            # 6. Compute tampering score (0.0 = clean, 1.0 = heavy manipulation)
            norm_mean = min(mean_diff / 25.0, 1.0)
            norm_var = min(patch_variance / 20.0, 1.0)
            tampering_score = float(0.4 * norm_mean + 0.6 * norm_var)

            # Determine risk level
            if tampering_score > 0.65 or max_diff > 180:
                risk_level = "HIGH"
                verdict = "Significant compression anomalies detected; localized high-frequency manipulation likely."
            elif tampering_score > 0.35:
                risk_level = "MODERATE"
                verdict = "Minor compression variance observed; possible re-saving, filtering, or partial editing."
            else:
                risk_level = "LOW"
                verdict = "Uniform error surface consistent with standard original compression profile."

            return {
                "success": True,
                "tool": "local_ela_analyzer",
                "tampering_score": round(tampering_score, 4),
                "risk_level": risk_level,
                "mean_difference": round(mean_diff, 2),
                "max_difference": round(max_diff, 2),
                "variance": round(patch_variance, 4),
                "verdict": verdict,
                "dimensions": f"{w}x{h}",
                "quality_tested": quality,
                "is_video": is_video,
                "ela_image_url": ela_image_url
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"ELA Analysis failed: {str(e)}"
            }
