import cv2
import numpy as np

cap = cv2.VideoCapture("C://Users//HARI//Downloads//Intro and loading Images  - OpenCV with Python for Image and Video Analysis 1.mp4")

while(True):
    ret , frame = cap.read()
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
