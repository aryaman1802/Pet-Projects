import torch
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
from PIL import Image

def load_model_info(path: str, device, model, model_name, optimizer, 
                    optimizer_name, scheduler=None, scheduler_name=""):
    if device == "cpu":    
        model.load_state_dict(torch.load(os.path.join(path, model_name), 
                                         map_location=torch.device('cpu')))
        model.to(device)
        optimizer.load_state_dict(torch.load(os.path.join(path, optimizer_name), 
                                             map_location=torch.device('cpu')))
        if scheduler is not None:
            scheduler.load_state_dict(torch.load(os.path.join(path, scheduler_name), 
                                                 map_location=torch.device('cpu')))
    print("Model info loaded!")
    

classes = {
    0: '0-2',
    1: '10-19',
    2: '20-29', 
    3: '3-9',
    4: '30-39', 
    5: '40-49', 
    6: '50-59', 
    7: '60-69',
    8: 'more than 70'
}


def predict(model, img_file, device, IMAGE_SIZE=224):
    img = Image.open(img_file).convert('RGB')
    augmentations = transforms.Compose([
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                             std=[0.229, 0.224, 0.225])
    ])
    img_tensor = augmentations(img)
    img_tensor = img_tensor.unsqueeze(dim=0)
    model.eval()
    with torch.inference_mode():
        img_tensor = img_tensor.to(device)
        # assuming model is already on the correct device
        output = model(img_tensor)
        probs = torch.softmax(output, dim=1)
        predicted_label = classes[probs.argmax(dim=1).cpu().detach().numpy().item()]
        label_prob = torch.max(probs) * 100
    return predicted_label, label_prob


