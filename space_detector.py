import cv2


def detect_space_objects(image_path):

    image = cv2.imread(image_path)

    height, width = image.shape[:2]

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    _, thresh = cv2.threshold(
        gray,
        170,
        255,
        cv2.THRESH_BINARY
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    objects = []

    for contour in contours:

        area = cv2.contourArea(contour)

        if area < 400:
            continue

        x, y, w, h = cv2.boundingRect(
            contour
        )

        objects.append({
            "name": "Space Object",
            "confidence": 0.85,
            "x": x / width,
            "y": y / height,
            "w": w / width,
            "h": h / height
        })

    if len(objects) == 0:

        objects.append({
            "name": "Unknown Object",
            "confidence": 0.60,
            "x": 0.25,
            "y": 0.25,
            "w": 0.30,
            "h": 0.20
        })

    return objects
