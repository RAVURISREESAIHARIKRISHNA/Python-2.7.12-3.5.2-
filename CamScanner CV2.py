#Build on Python 2.7.12
import cv2
import numpy as np

original = cv2.imread("G://Python DB//images//book.jpg")
img_color = cv2.imread("G://Python DB//images//book.jpg")
#img = cv2.imread("G://Python DB//images//book.jpg",0)
img_color = cv2.fastNlMeansDenoisingColored(img_color,None,10,10,7,21)
img = cv2.cvtColor(img_color , cv2.COLOR_BGR2GRAY)

#img = cv2.equalizeHist(img)

img = cv2.bilateralFilter(img , 9 ,75,75)
#Removing Blurness...
img_noblur = cv2.medianBlur(img , 3)

final_img = cv2.adaptiveThreshold(img, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 11 , 2)
final_img_1 = cv2.adaptiveThreshold(img , 255 ,cv2.ADAPTIVE_THRESH_MEAN_C  ,   cv2.THRESH_BINARY , 11 ,2)
cv2.namedWindow("Original" , cv2.WINDOW_NORMAL)
cv2.namedWindow("Processed" , cv2.WINDOW_NORMAL)
cv2.namedWindow("Processed 1" , cv2.WINDOW_NORMAL)

#final_img_no_blur = cv2.medianBlur(final_img ,7)
#final_img_1_no_blur = cv2.medianBlur(final_img_1 ,7)
#final_img_no_blur = cv2.fastNlMeansDenoisingColored(final_img,None,10,10,7,21)



final_img_1 = cv2.bilateralFilter(final_img_1 , 7 ,75,75)
final_img_1 = cv2.GaussianBlur(final_img_1 , (5,5) ,2)
final_img_1 = cv2.equalizeHist(final_img_1)
final_img = cv2.equalizeHist(final_img)
#kernel = np.ones((5,5),np.uint8)
#final_img_1 = cv2.erode(img , kernel ,iterations = 1)
cv2.imshow("Original",original)
cv2.imshow("Processed" , final_img)
cv2.imshow("Processed 1" , final_img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
