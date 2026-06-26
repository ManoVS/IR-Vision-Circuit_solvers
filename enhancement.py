import cv2
import numpy as np
import uuid
import os

OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def enhance_image(image_bytes):

    image = cv2.imdecode(
        np.frombuffer(
            image_bytes,
            np.uint8
        ),
        cv2.IMREAD_GRAYSCALE
    )

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(image)

    blur = cv2.GaussianBlur(
        enhanced,
        (0, 0),
        1
    )

    sharpened = cv2.addWeighted(
        enhanced,
        1.5,
        blur,
        -0.5,
        0
    )

    filename = f"enhanced_{uuid.uuid4()}.png"

    output_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    cv2.imwrite(
        output_path,
        sharpened
    )

    return output_path
