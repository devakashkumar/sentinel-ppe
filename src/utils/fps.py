import time
import cv2


class FPS:
    def __init__(self):
        self.prev_time = time.time()

    def draw(self, frame):
        current_time = time.time()
        fps = 1 / (current_time - self.prev_time)
        self.prev_time = current_time

        text = f"{int(fps)} FPS"

        (w, h), _ = cv2.getTextSize(
            text,
            cv2.FONT_HERSHEY_DUPLEX,
            0.7,
            2,
        )

        cv2.rectangle(
            frame,
            (15, 15),
            (30 + w, 50),
            (35, 35, 35),
            -1,
        )

        cv2.putText(
            frame,
            text,
            (22, 40),
            cv2.FONT_HERSHEY_DUPLEX,
            0.7,
            (0, 255, 255),
            2,
            cv2.LINE_AA,
        )

        return frame
