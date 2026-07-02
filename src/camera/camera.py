import cv2


class Camera:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(str(video_path))

        if not self.cap.isOpened():
            raise FileNotFoundError(f"Cannot open video: {video_path}")

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()
