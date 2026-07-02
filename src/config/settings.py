from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "model" / "ppe.pt"

# Change this to "sample2.mp4" whenever you want
VIDEO_NAME = "sample.mp4"

VIDEO_PATH = BASE_DIR / "videos" / VIDEO_NAME

WINDOW_NAME = "Sentinel PPE AI"

CONFIDENCE = 0.5
