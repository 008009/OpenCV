import os
from PIL import Image
import cv2
import pickle
import numpy as np

face_cascade = cv2.CascadeClassifier('/Users/carl0809/OpenCV/data/haarcascade_frontalface_default.xml')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
imageDir = os.path.join(BASE_DIR, "src")

#lbph recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
x_train = []
y_labels = []
for root, dirs, files in os.walk(imageDir):
	for file in files:
		if file.endswith("png"):
			imgPath = os.path.join(root, file)
			#print(imgPath)
			label = os.path.basename(root)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id_ = label_ids[label]
			#print(label_ids)
			#print(label)
			pil_image = Image.open(imgPath).convert("L")   #gray scale
			#resize image for training
			size = (550, 550)
			resize_image = pil_image.resize(size, Image.ANTIALIAS)
			img_Array = np.asarray(resize_image, "uint8")
			#print(img_Array)
			faces = face_cascade.detectMultiScale(img_Array, 1.3, 5)
			for(x, y, w, h) in faces:
				roi = img_Array[y:y+h, x:x+w]
				#print(roi)
				x_train.append(roi)
				y_labels.append(id_)
print(label_ids)

with open("labels.pickle", "wb") as f:
	pickle.dump(label_ids, f)

recognizer.train(x_train, np.asarray(y_labels))
recognizer.save("trainner.yml")