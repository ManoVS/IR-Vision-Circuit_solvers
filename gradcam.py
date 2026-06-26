import cv2
import numpy as np
import uuid
import os

OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_heatmap(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    heatmap = cv2.applyColorMap(
        gray,
        cv2.COLORMAP_JET
    )

    overlay = cv2.addWeighted(
        image,
        0.6,
        heatmap,
        0.4,
        0
    )

    filename = f"heatmap_{uuid.uuid4()}.png"

    output_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    cv2.imwrite(
        output_path,
        overlay
    )

    return output_path
