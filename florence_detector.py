from transformers import AutoProcessor
from transformers import AutoModelForCausalLM
from PIL import Image
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading Florence-2...")

processor = AutoProcessor.from_pretrained(
    "microsoft/Florence-2-base",
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Florence-2-base",
    trust_remote_code=True
).to(device)

print("Florence-2 loaded.")


def detect_scene(image_path):

    image = Image.open(image_path).convert("RGB")

    prompt = "<MORE_DETAILED_CAPTION>"

    inputs = processor(
        text=prompt,
        images=image,
        return_tensors="pt"
    ).to(device)

    with torch.no_grad():

        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=128
        )

    generated_text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return generated_text
