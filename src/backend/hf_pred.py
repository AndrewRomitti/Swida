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

    if predicted_label == "adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib":
        return "Adenocarcinoma"
    if predicted_label == "large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa" or predicted_label == "large.cell.carcinoma":
        return "Large Cell Carcinoma"
    if predicted_label == "squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa" or predicted_label == "squamous.cell.carcinoma":
        return "Squamous Cell Carcinoma"
    if predicted_label == "normal":
        return "Normal"
    return predicted_label
