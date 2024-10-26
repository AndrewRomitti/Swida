import transformers
import torch
from transformers import pipeline


def predict(given_image):
    MODEL_CHECKPOINT = "andrewromitti/Swida"
    DEIT_CHECKPOINT = "facebook/deit-base-distilled-patch16-224"

    validation_model = transformers.DeiTForImageClassification.from_pretrained(MODEL_CHECKPOINT,torch_dtype=torch.float16)
    image_processor = transformers.AutoImageProcessor.from_pretrained(DEIT_CHECKPOINT, return_tensors="pt")

    classifier = pipeline("image-classification", model=validation_model, image_processor=image_processor)
    results = classifier(given_image)
    max_result = max(results, key=lambda x: x['score'])
    predicted_label = max_result['label']

    return predicted_label
