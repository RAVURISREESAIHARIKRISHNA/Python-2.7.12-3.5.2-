#Build on Python 2.7.12
import cv2
import numpy as np

img1 = cv2.imread("G://Python DB//images//drive.png")#Default is Colour Image
img2 = cv2.imread("G://Python DB//images//sky.jpg")

add = img1 + img2

cvAdd = cv2.add(img1 , img2)
#//cvAdd1 = cv2.add(img1*2 , img2/2)

#Weighted Adding:
#This is Similar to cvAdd .In this Both the Images are given Equal Priorities and just got added up..Like (250,89,458)+(25,58,156) Giving (275,147,614)
#But in this we will Give Weights(Like 60%Weight for IMG1 and 40% Weight for IMG2) to each ImageOBJ to get added up
#Syntax:
#                                                    0.6(for 60%)                  0.4       0(Leave Gamma Value to 0)
#Weighted_Img_OBJ = cv2.addWeighted( Image_1_Object , Weight_1 , Image_2_Object , Weight_2 ,GammaValue)

Weighted_Image = cv2.addWeighted( img1 , 0.6 , img2 , 0.4 , 0)
Weighted_Image_50_50 = cv2.addWeighted( img1 , 1 , img2 , 0 , 10)#Shows img1

cv2.imshow("Drive",img1)
cv2.imshow("Sky",img2)
cv2.imshow("Added Image" , add)
cv2.imshow("CV Added Image" , cvAdd)
#//cv2.imshow("CV Added Image 1",cvAdd1)
cv2.imshow("Weighted Addded Image" , Weighted_Image)
cv2.imshow("Weighted Added Image 50,50",Weighted_Image_50_50)

cv2.waitKey(0)
cv2.destroyAllWindows()
