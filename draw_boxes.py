import cv2
import os
import uuid

OUTPUT_DIR = "outputs"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


def draw_boxes(image_path, objects):

    image = cv2.imread(image_path)

    if image is None:
        return image_path

    height, width = image.shape[:2]

    for obj in objects:

        x = int(obj["x"] * width)
        y = int(obj["y"] * height)

        w = int(obj["w"] * width)
        h = int(obj["h"] * height)

        label = (
            f'{obj["name"]} '
            f'{obj["confidence"]:.2f}'
        )

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.rectangle(
            image,
            (x, y - 30),
            (x + 180, y),
            (0, 255, 0),
            -1
        )

        cv2.putText(
            image,
            label,
            (x + 5, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2
        )

    filename = (
        "boxed_"
        + str(uuid.uuid4())
        + ".png"
    )

    output_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    cv2.imwrite(
        output_path,
        image
    )

    return output_path
