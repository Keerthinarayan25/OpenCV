import cv2 as cv
import sys

img = cv.imread("assets/preetham.jpg",0)
img=cv.resize(img,(0,0),fx=2, fy=2)
img=cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
img=cv.imwrite("new.jpg",img)
if img is None:
  sys.exit("Could not read the image")

cv.imshow("Diplay window",img)   

cv.waitKey(0)
cv.destroyAllWindows() 