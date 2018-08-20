import cv2
import sys
import pickle

img = cv2.imread(sys.argv[1])
face_cascade = cv2.CascadeClassifier('/Users/carl0809/OpenCV/data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

reverse_labels = {}
with open("labels.pickle", "rb") as f:
	old_labels = pickle.load(f)
	reverse_labels = {v: k for k, v in old_labels.items()}

height, width = img.shape[:2]
print(width)
print(height)

#need to convert to gray than detect face
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
face_color = (255, 0, 0) # BGR
stroke = 2

for (x,y,w,h) in faces:
	roi_gray = gray[y:y+h, x:x+w]
	id_, conf = recognizer.predict(roi_gray)
	print(conf)
	# if conf < 50 :
	# 	print("I am not confident enough to make predictions")
	# 	break
	# else:
	# 	name = reverse_labels[id_]
	name = reverse_labels[id_]
	cv2.rectangle(img, (x, y), (x+w, y+h), face_color, stroke)
	text = len(faces)
	font = cv2.FONT_HERSHEY_SIMPLEX
	face_color = (0, 0, 255)
	name_color = (255, 255, 255)
	cv2.putText(img, str(text) + " faces detected ", (5,15), font, 0.4, face_color, lineType=cv2.LINE_AA)
	cv2.putText(img, name, (x,y), font, 0.8, name_color, lineType=cv2.LINE_AA)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
