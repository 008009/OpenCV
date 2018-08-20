import cv2

face_cascade = cv2.CascadeClassifier('/Users/carl0809/Desktop/OpenCV/data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while (True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	face_color = (255, 0, 0) # BGR 
	stroke = 2
	for(x,y,w,h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), face_color, stroke)
		print(x, y, x+w, y+h)
		text = len(faces)
		cv2.putText(
    		frame, 
    		str(text) + " faces detected ", 
    		(5, 15), 
    		cv2.FONT_HERSHEY_SIMPLEX, 
    		0.4, 
    		(0, 0, 255), 
    		lineType=cv2.LINE_AA)
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

	
cap.release()
cv2.destroyAllWindows()
