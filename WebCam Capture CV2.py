#Build on Python 2.7.12
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*"XVID")
#OutVideo = cv2.VideoWriter("G://Python DB//Output.avi",fourcc , 10.0 ,(640,360))

while True:
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow("WebCam",frame)
   # OutVideo.write(frame)
    cv2.imshow("WebCam Gray",gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#OutVideo.release()

cv2.destroyAllWindows()
