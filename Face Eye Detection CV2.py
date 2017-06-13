#Build on Python 2.7.12
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('C://opencv//sources//data//haarcascades//haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C://opencv//sources//data//haarcascades//haarcascade_eye.xml')

img = cv2.imread("G://Python DB//images//face sample2.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
faces = face_cascade.detectMultiScale(gray , 1.3 , 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img , (x,y) ,(x+w , y+h) ,(0,0,255) , 0)
    roi_gray = gray[y:y+h , x:x+h]
    roi_color = img[y:y+h , x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color , (ex ,ey) , (ex+ew , ey+eh) , (0,255,0) , 0)

cv2.imshow("FACE AND EYE DETECTION" ,img)

cv2.waitKey(0)
cv2.destroyAllWindows()
