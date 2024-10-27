import torch
from PIL import Image
import numpy as np
from pytorch_grad_cam import GradCAMPlusPlus
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
from pytorch_grad_cam.utils.image import show_cam_on_image
from torchvision.models import resnet50
import torch.nn as nn
from torchvision import transforms
import os

def compute_gradcam(img, STATE_DICT_PATH="../../model_code/model_ft_3.pt", NUM_CLASSES=4):
    model = resnet50(pretrained=True)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, NUM_CLASSES)

    state_dict = torch.load(STATE_DICT_PATH, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)

    target_layers = [model.layer4[-1]]

    image = Image.open(img)
    image = image.convert('RGB')
    rgb_img = image.resize( (224, 224) )

    rgb_img = np.array(rgb_img).astype(np.float32) / 255.0

    transform1 = transforms.Resize((224,224))
    transform2 = transforms.ToTensor()
    input_tensor = transform1(image)
    input_tensor = transform2(input_tensor).cpu().unsqueeze(0)

    min_val = input_tensor.min()
    max_val = input_tensor.max()
    normalized_tensor = (input_tensor - min_val) / (max_val - min_val)
    input_tensor = normalized_tensor.type(torch.float32)

    targets = [ClassifierOutputTarget(2)]

    with GradCAMPlusPlus(model=model, target_layers=target_layers) as cam:
        grayscale_cam = cam(input_tensor=input_tensor, targets=targets)
        grayscale_cam = grayscale_cam[0, :]
        visualization = show_cam_on_image(rgb_img, grayscale_cam, use_rgb=True)
    
    return_img = Image.fromarray(visualization)

    file_name = os.path.basename(img)
    return_img.save('./uploads/images/grad_'+file_name)
    return return_img

