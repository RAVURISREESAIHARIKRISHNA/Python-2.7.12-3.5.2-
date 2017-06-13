import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('C://opencv//sources//data//haarcascades//haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C://opencv//sources//data//haarcascades//haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
	ret , frame = cap.read()
	
	frame_gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(frame_gray , 1.3 , 5)
	
	for (x,y,w,h) in faces:
		frame = cv2.rectangle( frame , (x,y) , (x+w , y+h) , (0,0,255) , 0)
		roi_frame_gray = frame_gray[y:y+h , x:x+h]
		roi_frame = frame[y:y+h , x:x+h]
		eyes = eye_cascade.detectMultiScale(roi_frame_gray)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_frame , (ex,ey) , (ex+ew , ey+eh) , (0,255,0) , 0)
			
	cv2.imshow("WebCam" , frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
