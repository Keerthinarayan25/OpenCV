import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
  print("Cannot Open Camera")
  exit()
while True:
  ret, frame = cap.read()
  width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #3
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #4

  image = np.zeros(frame.shape, np.uint8) #create an canvas so we can place as many videos on canvas  
  smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5) # shrink videos by height and width
  image[:height//2,:width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180) # top left
  gray = cv2.cvtColor(smaller_frame, cv2.COLOR_BGR2GRAY) #converts BGR to Gray color 
  gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) # converts Gray to BGR color
   # below here can't directly display 1 channel on black image canvas to we have to convert back to 3 channel but, still it is grayscale 
  image[height//2:,:width//2]= gray_bgr # bottom left
  image[:height//2,width//2:]=smaller_frame #top right
  image[height//2:,width//2:]=smaller_frame #bottom right

  cv2.imshow('frame',image)

  if cv2.waitKey(1)==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()

