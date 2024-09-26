import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

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

    
def predict(model, img_file, device):
    img = Image.open(img_file).convert('RGB')
    augmentations = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    img = augmentations(img)
    img = img.unsqueeze(dim=0)
    # print(f"Image shape: {img.shape}")
    model.eval()
    with torch.inference_mode():
        img = img.to(device)
        pred = model(img)
    # print(f"Prediction shape: {pred.shape}")
    pred_mask = pred.squeeze(dim=0).squeeze(dim=0).cpu().detach().numpy()
    # print(f"Prediction mask shape: {pred_mask.shape}")
    return pred_mask

