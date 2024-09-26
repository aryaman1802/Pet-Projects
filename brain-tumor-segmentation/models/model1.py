import torch
import torch.nn as nn

def double_conv(in_chan, out_chan):
    network = nn.Sequential(
        nn.Conv2d(in_channels=in_chan, out_channels=out_chan, kernel_size=(3,3), 
                  stride=1, padding=1, bias=False),
        nn.BatchNorm2d(out_chan),   # added new 
        nn.ReLU(inplace=True),
        nn.Conv2d(in_channels=out_chan, out_channels=out_chan, kernel_size=(3,3), 
                  stride=1, padding=1, bias=False),
        nn.BatchNorm2d(out_chan),   # added new 
        nn.ReLU(inplace=True)
    )
    return network


def crop_img(original: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    original_size = original.size()[2]
    target_size = target.size()[2]
    idx1 = (original_size - target_size)//2
    idx2 = original_size - idx1
    return original[:, :, idx1:idx2, idx1:idx2]


class UNet1(nn.Module):
    def __init__(self):
        super(UNet1, self).__init__()
        self.maxpool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.downconv1 = double_conv(1, 64)
        self.downconv2 = double_conv(64, 128)
        self.downconv3 = double_conv(128, 256)
        self.downconv4 = double_conv(256, 512)
        self.downconv5 = double_conv(512, 1024)
        self.trans1 = nn.ConvTranspose2d(1024, 512, kernel_size=2, stride=2)
        self.upconv1 = double_conv(1024, 512)
        self.trans2 = nn.ConvTranspose2d(512, 256, kernel_size=2, stride=2)
        self.upconv2 = double_conv(512, 256)
        self.trans3 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.upconv3 = double_conv(256, 128)
        self.trans4 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.upconv4 = double_conv(128, 64)
        self.out = nn.Conv2d(64, 1, kernel_size=1)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, img):
        # ENCODER
        x1 = self.downconv1(img)
        x2 = self.maxpool(x1)
        x3 = self.downconv2(x2)
        x4 = self.maxpool(x3)
        x5 = self.downconv3(x4)
        x6 = self.maxpool(x5)
        x7 = self.downconv4(x6)
        x8 = self.maxpool(x7)
        x9 = self.downconv5(x8)
        # DECODER
        a = self.trans1(x9)
        b = crop_img(x7, a)
        c = torch.cat([a,b], 1)
        d = self.upconv1(c)
        a = self.trans2(d)
        b = crop_img(x5, a)
        c = torch.cat([a,b], 1)
        d = self.upconv2(c)
        a = self.trans3(d)
        b = crop_img(x3, a)
        c = torch.cat([a,b], 1)
        d = self.upconv3(c)
        a = self.trans4(d)
        b = crop_img(x1, a)
        c = torch.cat([a,b], 1)
        d = self.upconv4(c)
        # we do sigmoid in the end, as we normalized our images and masks and 
        # sigmoid helps us output the model's predicted images in the 0 and 1 range
        out = self.sigmoid(self.out(d))
        return out