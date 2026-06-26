from transformers import AutoProcessor
from transformers import AutoModelForZeroShotObjectDetection
from PIL import Image
import torch

print("Loading Grounding DINO on CPU...")

processor = AutoProcessor.from_pretrained(
    "IDEA-Research/grounding-dino-base"
)

model = AutoModelForZeroShotObjectDetection.from_pretrained(
    "IDEA-Research/grounding-dino-base"
)

model = model.cpu()

print("Grounding DINO loaded.")


def detect_space_objects(image_path):

    image = Image.open(image_path).convert("RGB")

    prompt = (
        "satellite . spacecraft . solar panel . "
        "antenna . rocket . debris . planet . moon"
    )

    inputs = processor(
        images=image,
        text=prompt,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    results = processor.post_process_grounded_object_detection(
        outputs,
        inputs.input_ids,
        box_threshold=0.3,
        text_threshold=0.25,
        target_sizes=[image.size[::-1]]
    )

    objects = []

    for box, score, label in zip(
        results[0]["boxes"],
        results[0]["scores"],
        results[0]["labels"]
    ):

        x1, y1, x2, y2 = box.tolist()

        objects.append({
            "name": str(label),
            "confidence": float(score),
            "x": x1 / image.width,
            "y": y1 / image.height,
            "w": (x2 - x1) / image.width,
            "h": (y2 - y1) / image.height
        })

    return objects
