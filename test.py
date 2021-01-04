import os
import cv2
import sys
import random
import math
import re
import time
import skimage
import numpy as np
from image_converter.c2e import c2e
from image_converter.e2c import e2c
import tensorflow as tf
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log

import person

config = person.personConfig()

class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

with tf.device("/gpu:0"):
    model = modellib.MaskRCNN(mode="inference",config=config,model_dir='models/')

model.load_weights("models/mask_rcnn_person_0017.h5", by_name=True)
imgs=os.listdir('val')
img_size=1024
ksize = (100, 100)
for img in imgs:
    image=cv2.imread('val/'+img)
    cubemap=e2c(image, face_w=1024, mode='bilinear', cube_format='dice')
    blurred_cubemap=cv2.blur(cubemap, ksize)
    width=0
    img_size=1024
    while width<cubemap.shape[1]:                                                                                                           #Crop image to remove memory errors
        height=0
        while height<cubemap.shape[0]:
            cube=cubemap[height:height+img_size,width:width+img_size,0:3]
            blurred_cube=blurred_cubemap[height:height+img_size,width:width+img_size,0:3]
            cube_inverted=cv2.cvtColor(cube ,cv2.COLOR_RGB2BGR)
            result = model.detect([cube_inverted], verbose=0)
            result=result[0]
            mask=result['masks']
            N = result['rois'].shape[0]
            for i in range(N):
                px,py=np.where(mask[:, :, i]==True)
                for p in range(len(px)):
                    cube[px[p],py[p]]=blurred_cube[px[p],py[p]]
            cubemap[height:height+img_size,width:width+img_size,0:3]=cube
            height=height+1024
        width=width+1024
    
    cubemap=c2e(cubemap,image.shape[0],image.shape[1])
    cv2.imwrite('result_val/'+img,cubemap)
