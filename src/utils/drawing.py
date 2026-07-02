import cv2


BOX_COLOR = (255, 170, 0)      # Orange
TEXT_COLOR = (255, 255, 255)   # White
LABEL_BG = (35, 35, 35)        # Dark Gray


def draw_corner_box(img, x1, y1, x2, y2, color, thickness=2, length=18):
    # Top Left
    cv2.line(img, (x1, y1), (x1 + length, y1), color, thickness, cv2.LINE_AA)
    cv2.line(img, (x1, y1), (x1, y1 + length), color, thickness, cv2.LINE_AA)

    # Top Right
    cv2.line(img, (x2, y1), (x2 - length, y1), color, thickness, cv2.LINE_AA)
    cv2.line(img, (x2, y1), (x2, y1 + length), color, thickness, cv2.LINE_AA)

    # Bottom Left
    cv2.line(img, (x1, y2), (x1 + length, y2), color, thickness, cv2.LINE_AA)
    cv2.line(img, (x1, y2), (x1, y2 - length), color, thickness, cv2.LINE_AA)

    # Bottom Right
    cv2.line(img, (x2, y2), (x2 - length, y2), color, thickness, cv2.LINE_AA)
    cv2.line(img, (x2, y2), (x2, y2 - length), color, thickness, cv2.LINE_AA)


def draw_label(img, text, x, y):
    (w, h), _ = cv2.getTextSize(
        text,
        cv2.FONT_HERSHEY_DUPLEX,
        0.55,
        1,
    )

    cv2.rectangle(
        img,
        (x, y - h - 12),
        (x + w + 14, y),
        LABEL_BG,
        -1,
    )

    cv2.putText(
        img,
        text,
        (x + 7, y - 6),
        cv2.FONT_HERSHEY_DUPLEX,
        0.55,
        TEXT_COLOR,
        1,
        cv2.LINE_AA,
    )


def draw_detections(frame, results):
    for result in results:
        for box in result.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            conf = float(box.conf[0])
            cls = int(box.cls[0])

            label = f"{result.names[cls]}  {conf:.2f}"

            draw_corner_box(
                frame,
                x1,
                y1,
                x2,
                y2,
                BOX_COLOR,
                thickness=2,
            )

            draw_label(
                frame,
                label,
                x1,
                y1,
            )

    return frame
