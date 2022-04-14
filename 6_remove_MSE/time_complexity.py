from network import Net
from network_profile import LSE
from network_profile import FB2
from network_profile import MSE
from network_profile import FB1
from network_profile import HSE
from network_profile import HSE_UP

from ptflops import get_model_complexity_info
import torch
import torch.nn as nn
import time
from torchsummary import summary

class SID(nn.Module):
    def __init__(self):
        super(SID, self).__init__()
        
        self.up2 = nn.PixelShuffle(2)
        self.lrelu = nn.LeakyReLU(0.2, inplace=False)
        self.conv1_1 = nn.Conv2d(4, 32, kernel_size=3, stride=1, padding=1)
        self.conv1_2 = nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=1)
        self.pool1 = nn.MaxPool2d(kernel_size=2)
        
        self.conv2_1 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.conv2_2 = nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2)
        
        self.conv3_1 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.conv3_2 = nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1)
        self.pool3 = nn.MaxPool2d(kernel_size=2)
        
        self.conv4_1 = nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1)
        self.conv4_2 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)
        self.pool4 = nn.MaxPool2d(kernel_size=2)
        
        self.conv5_1 = nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1)
        self.conv5_2 = nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1)
        
        self.upv6 = nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.conv6_1 = nn.Conv2d(512, 256, kernel_size=3, stride=1, padding=1)
        self.conv6_2 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)
        
        self.upv7 = nn.ConvTranspose2d(256, 128, 2, stride=2)
        self.conv7_1 = nn.Conv2d(256, 128, kernel_size=3, stride=1, padding=1)
        self.conv7_2 = nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1)
        
        self.upv8 = nn.ConvTranspose2d(128, 64, 2, stride=2)
        self.conv8_1 = nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=1)
        self.conv8_2 = nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1)
        
        self.upv9 = nn.ConvTranspose2d(64, 32, 2, stride=2)
        self.conv9_1 = nn.Conv2d(64, 32, kernel_size=3, stride=1, padding=1)
        self.conv9_2 = nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=1)
        
        self.conv10_1 = nn.Conv2d(32, 12, kernel_size=1, stride=1)
    
    def forward(self, x):
        conv1 = self.lrelu(self.conv1_1(self.downshuffle(x,2)))
        conv1 = self.lrelu(self.conv1_2(conv1))
        pool1 = self.pool1(conv1)
        
        conv2 = self.lrelu(self.conv2_1(pool1))
        conv2 = self.lrelu(self.conv2_2(conv2))
        pool2 = self.pool1(conv2)
        
        conv3 = self.lrelu(self.conv3_1(pool2))
        conv3 = self.lrelu(self.conv3_2(conv3))
        pool3 = self.pool1(conv3)
        
        conv4 = self.lrelu(self.conv4_1(pool3))
        conv4 = self.lrelu(self.conv4_2(conv4))
        pool4 = self.pool1(conv4)
        
        conv5 = self.lrelu(self.conv5_1(pool4))
        conv5 = self.lrelu(self.conv5_2(conv5))
        
        up6 = self.upv6(conv5)
        up6 = torch.cat([up6, conv4], 1)
        conv6 = self.lrelu(self.conv6_1(up6))
        conv6 = self.lrelu(self.conv6_2(conv6))
        
        up7 = self.upv7(conv6)
        up7 = torch.cat([up7, conv3], 1)
        conv7 = self.lrelu(self.conv7_1(up7))
        conv7 = self.lrelu(self.conv7_2(conv7))
        
        up8 = self.upv8(conv7)
        up8 = torch.cat([up8, conv2], 1)
        conv8 = self.lrelu(self.conv8_1(up8))
        conv8 = self.lrelu(self.conv8_2(conv8))
        
        up9 = self.upv9(conv8)
        up9 = torch.cat([up9, conv1], 1)
        conv9 = self.lrelu(self.conv9_1(up9))
        conv9 = self.lrelu(self.conv9_2(conv9))
        
        conv10= self.conv10_1(conv9)
        out = self.up2(conv10)
        return out
    
    def downshuffle(self,var,r):
        b,c,h,w = var.size()
        out_channel = c*(r**2)
        out_h = h//r
        out_w = w//r
        return var.contiguous().view(b, c, out_h, r, out_w, r).permute(0,1,3,5,2,4).contiguous().view(b,out_channel, out_h, out_w).contiguous()


model_ours = Net()
model_sid = SID()

model_lse = LSE()
model_fb2 = FB2()
model_mse = MSE()
model_fb1 = FB1()
model_hse = HSE()
model_hseup = HSE_UP()

print('\n---Our Model parameters : {}\n'.format(sum(p.numel() for p in model_ours.parameters() if p.requires_grad)))
print('\n---SID model parameters : {}\n'.format(sum(p.numel() for p in model_sid.parameters() if p.requires_grad)))

print('\n---LSE Model parameters : {}\n'.format(sum(p.numel() for p in model_lse.parameters() if p.requires_grad)))
print('\n---FB2 Model parameters : {}\n'.format(sum(p.numel() for p in model_fb2.parameters() if p.requires_grad)))
'''
print('\n---MSE model parameters : {}\n'.format(sum(p.numel() for p in model_mse.parameters() if p.requires_grad)))
print('\n---FB1 model parameters : {}\n'.format(sum(p.numel() for p in model_fb1.parameters() if p.requires_grad)))
'''
print('\n---HSE model parameters : {}\n'.format(sum(p.numel() for p in model_hse.parameters() if p.requires_grad)))
print('\n---HSEup model parameters : {}\n'.format(sum(p.numel() for p in model_hseup.parameters() if p.requires_grad)))


H = (2048//32)*32
W = (4096//32)*32

zero_count = 0
for param in model_ours.parameters():
    if param is not None:
        x = param.data == 0
        zero_count += torch.sum(x)
print("zeros org: {}".format(zero_count))

'''
for param in model_ours.parameters():
    if param is not None:
        param.data = param.data.type(dtype=torch.float16)
        param.data = param.data.type(dtype=torch.float32)

zero_count = 0
for param in model_ours.parameters():
    if param is not None:
        x = param.data == 0
        zero_count += torch.sum(x)
print("zeros float16: {}".format(zero_count))

thres = 0.015625 #(1/2^6)
for param in model_ours.parameters():
    if param is not None:
        param.data[abs(param.data) < thres ] = 0

zero_count = 0
for param in model_ours.parameters():
    if param is not None:
        x = param.data == 0
        zero_count += torch.sum(x)
print("zeros zero-out: {}".format(zero_count))
'''
summary(model_ours, (1, H, W), device='cpu')

macs, params = get_model_complexity_info(model_ours, (1, H,W), as_strings=False,
                                       print_per_layer_stat=True, verbose=True)
print('{:<30}  {:<8}'.format('Computational complexity of Our model for a 8MP image: ', macs))
macs, params = get_model_complexity_info(model_sid, (1, H,W), as_strings=True,
                                       print_per_layer_stat=False, verbose=False)
print('{:<30}  {:<8}'.format('Computational complexity of SID model for a 8MP image: ', macs))

#### LSE
macs, params = get_model_complexity_info(model_lse, (4, H//2,W//2), as_strings=True,
                                       print_per_layer_stat=False, verbose=False)
print('{:<30}  {:<8}'.format('Computational complexity of model_lse model for a 8MP/2 image: ', macs))

macs, params = get_model_complexity_info(model_fb2, (24, H//2,W//2), as_strings=True,
                                       print_per_layer_stat=False, verbose=False)
print('{:<30}  {:<8}'.format('Computational complexity of model_fb2 model for a 8MP/2 image: ', macs))

#### MSE
'''
macs, params = get_model_complexity_info(model_mse, (64, H//8,W//8), as_strings=True,
                                       print_per_layer_stat=False, verbose=False)
print('{:<30}  {:<8}'.format('Computational complexity of model_mse model for a 8MP/8 image: ', macs))

macs, params = get_model_complexity_info(model_fb1, (128, H//8,W//8), as_strings=True,
                                       print_per_layer_stat=False, verbose=False)
print('{:<30}  {:<8}'.format('Computational complexity of model_fb1 model for a 8MP/8 image: ', macs))
'''
#### HSE
macs, params = get_model_complexity_info(model_hse, (1024, H//32,W//32), as_strings=True,
                                       print_per_layer_stat=False, verbose=False)
print('{:<30}  {:<8}'.format('Computational complexity of model_hse model for a 8MP/16 image: ', macs))

macs, params = get_model_complexity_info(model_hseup, (64, H//32,W//32), as_strings=True,
                                       print_per_layer_stat=False, verbose=False)
print('{:<30}  {:<8}'.format('Computational complexity of model_hseup model for a 8MP/16 image: ', macs))

tensor = torch.rand(1,1,H,W)
with torch.no_grad():
    model_ours.eval()
    model_sid.eval()
    print('Beginning Warmup...')
    model_ours(tensor) # warmup
    model_sid(tensor) # warmup
    
    beg=time.time()
    for i in range(5):
        model_ours(tensor)
    print('Time taken by our model on CPU for 8MP image : {} seconds'.format((time.time()-beg)/5))

    beg=time.time()
    for i in range(5):
        model_sid(tensor)
    print('Time taken by SID model on CPU for 8MP image : {} seconds'.format((time.time()-beg)/5))

    #### LSE
    tensor = torch.rand(1, 4, H//2,W//2)
    beg=time.time()
    for i in range(5):
        model_lse(tensor)
    print('Time taken by model_lse on CPU for 8MP/2 image : {} seconds'.format((time.time()-beg)/5))

    tensor = torch.rand(1,24, H//2,W//2)
    beg=time.time()
    for i in range(5):
        model_fb2(tensor)
    print('Time taken by model_fb2 on CPU for 8MP/2 image : {} seconds'.format((time.time()-beg)/5))

    #### MSE
    '''
    tensor = torch.rand(1, 64, H//8,W//8)
    beg=time.time()
    for i in range(5):
        model_mse(tensor)
    print('Time taken by model_mse on CPU for 8MP/8 image : {} seconds'.format((time.time()-beg)/5))

    tensor = torch.rand(1, 128, H//8,W//8)
    beg=time.time()
    for i in range(5):
        model_fb1(tensor)
    print('Time taken by model_fb1 on CPU for 8MP/8 image : {} seconds'.format((time.time()-beg)/5))
    '''

    #### HSE
    tensor = torch.rand(1, 1024, H//32,W//32)
    beg=time.time()
    for i in range(5):
        model_hse(tensor)
    print('Time taken by model_hse on CPU for 8MP/32 image : {} seconds'.format((time.time()-beg)/5))

    tensor = torch.rand(1, 64, H//32,W//32)
    beg=time.time()
    for i in range(5):
        model_hseup(tensor)
    print('Time taken by model_hseup on CPU for 8MP/32 image : {} seconds'.format((time.time()-beg)/5))
