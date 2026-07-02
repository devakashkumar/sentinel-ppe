import cv2
from pathlib import Path

from src.camera.camera import Camera
from src.detection.detector import Detector
from src.utils.drawing import draw_detections
from src.utils.fps import FPS
from src.config.settings import (
    MODEL_PATH,
    VIDEO_PATH,
    WINDOW_NAME,
    CONFIDENCE,
)


class Pipeline:
    def __init__(self):
        self.camera = Camera(VIDEO_PATH)
        self.detector = Detector(MODEL_PATH, CONFIDENCE)
        self.fps = FPS()

    def run(self):
        success, frame = self.camera.read()

        if not success:
            print("Failed to open video.")
            return

        height, width = frame.shape[:2]
        fps = self.camera.cap.get(cv2.CAP_PROP_FPS)

        Path("outputs").mkdir(exist_ok=True)

        output_path = Path("outputs") / f"{VIDEO_PATH.stem}_output.mp4"

        writer = cv2.VideoWriter(
            str(output_path),
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (width, height),
        )

        while success:

            results = self.detector.detect(frame)

            frame = draw_detections(frame, results)
            frame = self.fps.draw(frame)

            writer.write(frame)

            cv2.imshow(WINDOW_NAME, frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            success, frame = self.camera.read()

        writer.release()
        self.camera.release()
        cv2.destroyAllWindows()

        print(f"\n✅ Output saved to: {output_path}")
