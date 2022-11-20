import os
import cv2
import numpy as np
from PIL import Image as im

from eigenfunction import eigen

faces_matrix = []

folders = os.listdir("../dataset/")
for folder in folders:
	picts = os.listdir("../dataset/" + folder + "/")
	for pict in picts:
		print("Processing: " + "../dataset/" + folder + "/" + pict)
		img = im.open("../dataset/" + folder + "/" + pict).convert("L")
		img = img.resize((256,256), im.BICUBIC)
		img = np.array(img).flatten()
		faces_matrix.append(img)

# m adalah jumlah wajah dalam dataset
m = len(faces_matrix)

# faces_matrix -> M x N^2
faces_matrix = np.vstack(faces_matrix)

# hitung mean face
mean_face = np.mean(faces_matrix, axis=0)

# "normal"kan wajah training (face - average face)
for i in range(m):
	faces_matrix[i] = faces_matrix[i] - mean_face

# face_matrix adalah "normal" dari wajah, bukan matriks citra wajah
faces_matrix = np.transpose(faces_matrix)
# faces_matrix -> N^2 x M

# C = A^T x A
C = np.transpose(faces_matrix) @ faces_matrix
# Matriks kovarian, C -> M x M

# Hitung nilai eigen dan vektor eigen C
EigVal, EigVect = eigen(C, 8000)
# EigVect adalah matriks dengan entri kolom ke-i vektor basis yang berkoresponden dengan nilai eigen ke-i EigVal

# EigFace adalam matriks wajah-wajah eigen, dengan entri kolom adalah vektor wajah
EigFace = []
for i in range(m):
	EigFace.append(faces_matrix @ EigVect[:,i])

EigFace = np.transpose(EigFace)

print("beres")
pict = input()
while(pict != "sex"):
	img = im.open("../temp/"+pict).convert("L")
	img = img.resize((256,256), im.BICUBIC)
	img = np.array(img).flatten()

	NewFace = img - mean_face
    
	k = -1
	min = 999999999999
	for i in range(m):
		epsilon = abs(np.dot(NewFace, faces_matrix @ EigVect[i]))
		print(i, epsilon)
		if (epsilon < min):
			min = epsilon
			k = i

# 	k = -1
# 	min = 9999999999999999999999999
# 	for i in range(m):
# 		epsilon = np.linalg.norm(NewFace - EigFace[:,i])
# # 		print(epsilon < min)
# 		if(epsilon < min):
# 			min = epsilon
# 			k = i

	print(k)
	pict = input()