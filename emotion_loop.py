import cv2
import torch
from torchvision import transforms
import math
import numpy as np
import torchvision.models as models
import torch.utils.data as data
from torchvision import transforms
import cv2
import torch.nn.functional as F
from torch.autograd import Variable
import pandas as pd
import os ,torch
import torch.nn as nn
import time
import argparse
import functions
from PIL import Image
import requests

result = ["Surprise","Fear","Disgust","Happiness","Sadness","Anger","Neutral"]

class Res18Feature(nn.Module):
  def __init__(self, pretrained, num_classes = 7):
    super(Res18Feature, self).__init__()
    resnet  = models.resnet18(pretrained)
    self.features = nn.Sequential(*list(resnet.children())[:-1]) 
    fc_in_dim = list(resnet.children())[-1].in_features 
    self.fc = nn.Linear(fc_in_dim, num_classes) 
    self.alpha = nn.Sequential(nn.Linear(fc_in_dim, 1),nn.Sigmoid())

  def forward(self, x):
    x = self.features(x)
    x = x.view(x.size(0), -1)
    attention_weights = self.alpha(x)
    out = attention_weights * self.fc(x)
    return attention_weights, out

model_save_path = "./checkpoint/wiki2020.pth" #mode path

def main():
  preprocess_transform = transforms.Compose([transforms.ToPILImage(),transforms.Resize((224, 224)),transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])
        
  res18 = Res18Feature(pretrained = False)
  checkpoint = torch.load(model_save_path, map_location=torch.device('cpu')) ##
  res18.load_state_dict(checkpoint['model_state_dict'])

  res18.eval()

  df = functions.read_excel()
  df = functions.limit_emotions(df)
  df['pred'] = 0

  for i in range(len(df['url_server'][:])):
    print('cycle Num:', i, '/1140')
    time1=time.time()

    url = df['url_server'][i]
    #print(url)
    req = requests.get(url, stream=True).raw.read()
    arr = np.frombuffer(req, np.uint8)
    im = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    #im = Image.open(requests.get(url, stream=True).raw)
    
    f_name, ext = os.path.splitext(url)
    img_name = f_name.split('/')[-1]

    functions.save_img(im, img_name, ext)

    image = np.array(im)
    #print(len(image))
    image = image[:, :, ::-1]
    image_tensor = preprocess_transform(image)
    tensor = Variable(torch.unsqueeze(image_tensor, dim=0).float(), requires_grad=False)
    time2=time.time()
    _, outputs = res18(tensor)
    _, predicts = torch.max(outputs, 1)
    #print(outputs)
    print(result[int(predicts.cpu().data)])

    df.loc[i, 'pred'] = result[int(predicts.cpu().data)]
    #print(df['pred'])
  #If you want to save the results
  #df.to_excel('1140Faces_WIKI2020_on_emotioNet.xlsx')

if __name__ == "__main__":
  main()
