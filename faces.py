import cv2
import sys

img = cv2.imread(sys.argv[1])
face_cascade = cv2.CascadeClassifier('/Users/carl0809/OpenCV/data/haarcascade_frontalface_default.xml')
height, width = img.shape[:2]
print(width)
print(height)

#need to convert to gray than detect face
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
face_color = (255, 0, 0) # BGR
stroke = 2

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), face_color, stroke)
    text = len(faces)
    cv2.putText(img, 
                str(text) + " faces detected ", 
                (5,15),
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.4, 
                (0, 0, 255), 
                lineType=cv2.LINE_AA)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
