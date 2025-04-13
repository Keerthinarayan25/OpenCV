import cv2 as cv
import sys

img = cv.imread("assets/dog.jpg",0) #reads the file
img=cv.resize(img,(0,0),fx=2, fy=2)  # shrik the height and width of image
img=cv.rotate(img,cv.ROTATE_90_CLOCKWISE) # rotate the image 
img=cv.imwrite("new.jpg",img) # saves the image in folder as "new.jpg"
if img is None:
  sys.exit("Could not read the image") # if file name didn't exist the message will be printed

cv.imshow("Diplay window",img)   

cv.waitKey(0) # "0" means wait until any key is pressed can give number as "4" this is in milli seconds 
cv.destroyAllWindows() 
