import cv2
import albumentations as A
import os
import sys
import json
from tqdm import tqdm

def getAllName(file_dir, tail_list = ['.JPG','.jpg']): #
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] in tail_list:
                L.append(os.path.join(root, file))
    return L

def process(img_path):
    img = cv2.imread(img_path)
    h,w = 600,600
    input_h, input_w = img.shape[:2]
    print(input_h,input_w)
    
    h_ratio = input_h/h
    w_ratio = input_w/w
    if (h_ratio>1 and w_ratio>1):
        if h_ratio>w_ratio:
            resize_h = h
            resize_w = int(input_w/h_ratio)
        else:
            resize_w = w
            resize_h = int(input_h/w_ratio)
        img = A.Resize(resize_h,resize_w,cv2.INTER_AREA)(image=img)['image']
        cv2.imwrite(img_path, img)	

imgs = getAllName('/media/qifubo/_data/smoking_calling/')
print(len(imgs))

for img_path in tqdm(imgs):
    try:
        process(img_path)
    except Exception as e:
        print(str(e))
        print(f"{img_path} is failed.")
    
#     img = cv2.imread(img_path)
#     h,w = 600,600
#     input_h, input_w = img.shape[:2]
#     h_ratio = input_h/h
#     w_ratio = input_w/w
#     if (h_ratio>1 and w_ratio>1):
#         if h_ratio>w_ratio:
#             resize_h = h
#             resize_w = int(input_w/h_ratio)
#         else:
#             resize_w = w
#             resize_h = int(input_h/w_ratio)
#         img = A.Resize(resize_h,resize_w,cv2.INTER_AREA)(image=img)['image']
#         cv2.imwrite(img_path, img)