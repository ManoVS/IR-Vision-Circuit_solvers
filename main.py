from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from enhancement import enhance_image
from colorization import colorize_image
from detection import detect_objects
from gradcam import generate_heatmap
from draw_boxes import draw_boxes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs"
)


@app.get("/")
def home():
    return {
        "status": "IRVision Running"
    }


@app.post("/pipeline")
async def pipeline(file: UploadFile = File(...)):

    image_bytes = await file.read()

    enhanced_path = enhance_image(
        image_bytes
    )

    colorized_path = colorize_image(
        enhanced_path
    )

    result = detect_objects(
        colorized_path
    )

    boxed_path = draw_boxes(
        colorized_path,
        result["objects"]
    )

    heatmap_path = generate_heatmap(
        colorized_path
    )

    result["enhanced_image"] = (
        enhanced_path.replace("\\", "/")
    )

    result["colorized_image"] = (
        colorized_path.replace("\\", "/")
    )

    result["heatmap"] = (
        heatmap_path.replace("\\", "/")
    )

    result["boxed_image"] = (
        boxed_path.replace("\\", "/")
    )

    return result
