import os
import cv2
import numpy as np
from PIL import Image as im

m
EigVect
EigFace

pict = input()
img = im.open("../test"+pict).convert("L")
img = img.resize((256,256), im.BICUBIC)
img = np.array(img).flatten()

NewFace = img - mean_face
NewFace = EigVect @ NewFace

min = 9999
for i in range(m):
    epsilon = np.linalg.norm(NewFace - EigFace[:,i])
    if(epsilon < min):
        min = epsilon
        k = i
