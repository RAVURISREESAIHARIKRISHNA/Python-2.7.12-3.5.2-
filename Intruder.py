#Built on Python 2.7.12

#Sir,this Program has Console and not yet been made Terminative Resistant

#Open CV Library,numpy,matplotlib are Must Libraries for Running this...
#They are not available by Default
import cv2
import numpy as np
import sys
import matplotlib

#Accessing WebCam (Default one by specifying o)
#Firing the WebCam if it is Available
cap = cv2.VideoCapture(0)

#Returns True to the ret if a Frame from WebCam is availabe
#if so ,it returns the Frame to frame from WebCam
ret,frame = cap.read()

#Creating a GUI Window to show the Intruder...
#If we want the frame can be saved as .png file in the desired location
cv2.imshow("Intruder",frame)
cap.release()

#Waiting for a Key to be pressed,to Close
if cv2.waitKey(0):
    #cap.release()
    cv2.destroyAllWindows()
    sys.exit(0)
