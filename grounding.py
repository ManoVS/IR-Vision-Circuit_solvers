from PIL import Image


def detect_boxes(image_path, description):

    image = Image.open(image_path)

    width, height = image.size

    objects = []

    description = description.lower()

    if "satellite" in description:
        objects.append({
            "name": "Satellite",
            "confidence": 0.90,
            "x": 0.25,
            "y": 0.20,
            "w": 0.35,
            "h": 0.20
        })

    if "rocket" in description:
        objects.append({
            "name": "Rocket",
            "confidence": 0.88,
            "x": 0.40,
            "y": 0.15,
            "w": 0.20,
            "h": 0.50
        })

    if "planet" in description:
        objects.append({
            "name": "Planet",
            "confidence": 0.92,
            "x": 0.20,
            "y": 0.20,
            "w": 0.50,
            "h": 0.50
        })

    if "spacecraft" in description:
        objects.append({
            "name": "Spacecraft",
            "confidence": 0.87,
            "x": 0.30,
            "y": 0.30,
            "w": 0.30,
            "h": 0.25
        })

    if len(objects) == 0:
        objects.append({
            "name": "Unknown Space Object",
            "confidence": 0.60,
            "x": 0.25,
            "y": 0.25,
            "w": 0.30,
            "h": 0.20
        })

    return objects
