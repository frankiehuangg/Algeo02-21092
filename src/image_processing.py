import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image as im

neutral = []

folders = os.listdir("../dataset/")
for folder in folders:
	picts = os.listdir("../dataset/" + folder + "/")
	for pict in picts:
		print("Processing: " + "../dataset/" + folder + "/" + pict)
		img = im.open("../dataset/" + folder + "/" + pict).convert("L")
		img = img.resize((256,256), im.BICUBIC)
		img = np.array(img).flatten()
		neutral.append(img)

faces_matrix = np.vstack(neutral)
print(faces_matrix.shape)

mean_face = np.mean(faces_matrix, axis=0).reshape(256,256)
print(mean_face.shape)

cv2.imwrite("output.jpg", mean_face)