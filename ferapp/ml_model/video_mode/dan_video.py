from PIL import Image
import numpy as np
import cv2
import ferapp.ml_model.video_mode.video_to_frames_divider as vfd
import datetime
import os, glob


import torch
from torchvision import transforms
from ferapp.ml_model.video_mode.network.dan import DAN

class Model():
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.data_transforms = transforms.Compose([
                                    transforms.Resize((224, 224)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
                                ])
        self.labels = ['neutral', 'happy', 'sad', 'surprise', 'fear', 'disgust', 'anger', 'contempt']

        self.model = DAN(num_head=4, num_class=8, pretrained=False)
        checkpoint = torch.load(r'ferapp\ml_model\image_mode\checkpoints\affecnet8_epoch5_acc0.6209.pth',
            map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'],strict=True)
        self.model.to(self.device)
        self.model.eval()

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    
    def detect(self, img0):
        img = cv2.cvtColor(np.asarray(img0),cv2.COLOR_RGB2BGR)
        faces = self.face_cascade.detectMultiScale(img)
        
        return faces

    def fer(self, path):
        labels=[]
        coordinates=[]
        img0 = Image.open(path).convert('RGB')

        faces = self.detect(img0)

        if len(faces) == 0:
            return 'null'
        
        for face_index in range(len(faces)):
            x, y, w, h = faces[face_index]
            img = img0.crop((x,y, x+w, y+h))

            img = self.data_transforms(img)
            img = img.view(1,3,224,224)
            img = img.to(self.device)

            with torch.set_grad_enabled(False):
                out, _, _ = self.model(img)
                _, pred = torch.max(out,1)
                index = int(pred)
                label = self.labels[index]
                labels.append(label)
                coord=str(x)+', '+str(y)+', '+str(w)+', '+str(h)
                coordinates.append(coord)
        return labels, coordinates
         
def image_analyzer(image, count, file, fps):
    model = Model()
    label, coordinates = model.fer(image)
    seconds = round(count / fps)
    video_time = datetime.timedelta(seconds=seconds)
    for x in range(len(label)):
        file.writelines(label[x] +' : ')
        file.writelines(coordinates[x]+' : ')
        file.writelines(str(video_time)+' : ')
        file.writelines("frame"+' '+str(count))
        file.write('\n')


def main(video, vid_title):
    dir = 'ferapp\ml_model\\video_mode\\frames'
    for file in os.scandir(dir):
        os.remove(file.path)
    fps,frames=vfd.video_divider(vid_title)
    fp=open('ferapp\ml_model\\video_mode\emotion.txt','w')
    for x in range(int(frames)):
        img=str("ferapp\ml_model\\video_mode\\frames\\frame"+str(x+1)+".jpg")
        image_analyzer(img, x+1, fp, fps)
    fp.close()
