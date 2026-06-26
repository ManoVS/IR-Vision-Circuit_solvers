from florence_detector import detect_scene
from grounding_detector import detect_space_objects
from space_knowledge import get_object_information


def detect_objects(image_path):

    description = detect_scene(
        image_path
    )

    objects = detect_space_objects(
        image_path
    )

    information = get_object_information(
        objects
    )

    return {
        "scene": "space",
        "scene_description": description,
        "objects": objects,
        "information": information
    }
