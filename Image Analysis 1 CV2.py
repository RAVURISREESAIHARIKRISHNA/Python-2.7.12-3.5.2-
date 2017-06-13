#Build on Python 2.7.12
import numpy as np
import cv2

img = cv2.imread("G://Python DB//images//drive.png" , cv2.IMREAD_COLOR)

Reg = img[100:185 , 26:256]
img[0:85 , 0:230] =Reg
img[427:512 , 282:512] = Reg
img[427:512 , 282:512] = img[50:135 , 16:246]
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.imwrite("G://Python DB//images//drive Morphed.png",img)
cv2.destroyAllWindows()
