SPACE_DATABASE = {
    "satellite": {
        "description":
            "Artificial object orbiting Earth.",
        "applications": [
            "Communication",
            "Navigation",
            "Earth observation"
        ]
    },

    "spacecraft": {
        "description":
            "Vehicle operating in outer space.",
        "applications": [
            "Exploration",
            "Research"
        ]
    },

    "rocket": {
        "description":
            "Launch vehicle used to place payloads into orbit.",
        "applications": [
            "Launch missions"
        ]
    },

    "solar panel": {
        "description":
            "Power generation unit.",
        "applications": [
            "Electrical power"
        ]
    },

    "antenna": {
        "description":
            "Communication system.",
        "applications": [
            "Telemetry",
            "Communication"
        ]
    },

    "planet": {
        "description":
            "Celestial body orbiting a star.",
        "applications": [
            "Astronomical study"
        ]
    }
}


def get_object_information(objects):

    info = []

    for obj in objects:

        label = obj["name"].lower()

        if label in SPACE_DATABASE:

            info.append({
                "name": obj["name"],
                "description":
                    SPACE_DATABASE[label]["description"],
                "applications":
                    SPACE_DATABASE[label]["applications"]
            })

    return info
