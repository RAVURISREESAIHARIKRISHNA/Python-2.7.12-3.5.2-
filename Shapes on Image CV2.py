#Build on Python 2.7.12
import numpy as np
import cv2

img = cv2.imread("G://Python DB//images//drive.png",cv2.IMREAD_COLOR)


#cv2.line(ImageOBJ , (x1,y1) , (x2,y2) , (Blue amount , Green Amount , Red Amount) , PixelWidth of the Line)
# B,G,R Amount cannot be greater than 255

# When B=G=R=255 it will be WHITE

cv2.line(img , (0,0) , (120,340) , (255,45,187) , 3)
#This will just draw the Line on the Image(IT WILL NOT SHOW ON SCREEN UNLESS YOU imshow IT)
#After Drawing the Figure,we should show the image

#cv2.rectangle( ImageOBJ , (x1,y1) , (x4,y4) , (Blue Amount , Green Amount , Red Amount) , PixelWidth of THe Line)

#If Negative PixeWidth of the Line is given,Then it will Fill-up the Figure

cv2.rectangle( img , (156,156) , (356,356) , (145,4,245) , -1)

#                       centere
#cv2.circle(ImageOBJ , (x,y) , r , (Blue Amount , Green Amount , Red Amount) , PixelWidth of the Line)
cv2.circle(img , (256,256) , 100 , (0,255,255) ,4)

#cv2.putText(ImageOBJ , "YourText" , (x,y) , FULLY QUALIFIED FONT NAME , SIZE OF LETTERS(int) ,(B,G,R), SPACE BETWEEN LETTERS(int) , Type oF LINE)
cv2.putText(img , "Hello" , (256,256) , cv2.FONT_ITALIC , 1 , (255,255,0) , 2 , cv2.LINE_AA)



cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
