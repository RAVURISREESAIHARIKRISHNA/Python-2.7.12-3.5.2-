# Build on Python 2.7.12

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("G://Python DB//images//drive.png",cv2.IMREAD_GRAYSCALE)
# Use the foolwing line to show the actual Colour Image
# img = cv2.imread("G://Python DB//drive.png")

#cv2.imshow("WindowNamw",ImageOBJ)
cv2.imshow("image",img)

#Waits for any key to Press
cv2.waitKey(0)
cv2.imwrite("G://Python DB//images//drivegray.png",img)
cv2.destroyAllWindows()
