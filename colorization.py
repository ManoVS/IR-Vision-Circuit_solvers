import cv2
import numpy as np
import uuid
import os

OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def colorize_image(image_path):

    image = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    if image is None:
        return image_path

    normalized = cv2.normalize(
        image,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    colored = cv2.applyColorMap(
        normalized,
        cv2.COLORMAP_TURBO
    )

    filename = f"colorized_{uuid.uuid4()}.png"

    output_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    cv2.imwrite(
        output_path,
        colored
    )

    return output_path
