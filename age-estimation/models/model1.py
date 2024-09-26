import torch
import torch.nn as nn
import torchvision

class Model1(nn.Module):
    def __init__(self):
        super(Model1, self).__init__()
        # weights = torchvision.models.VGG16_Weights.DEFAULT
        # self.backbone = torchvision.models.vgg16(weights=weights)
        self.backbone = torchvision.models.vgg16(pretrained=True)
        for param in self.backbone.parameters():
            param.requires_grad = False
        self.backbone.avgpool = nn.Sequential(
            nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.Flatten()
        )
        self.backbone.classifier = nn.Sequential(
            nn.Linear(2048,512),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(512,128),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64, 10),
        )
        
    def forward(self, x):
        x = self.backbone(x)
        return x
    
