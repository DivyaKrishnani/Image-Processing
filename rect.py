import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

#To draw a rectangle, you need top-left corner and bottom-right corner of rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.rectangle(img,(0,0),(511,511),(255,0,0),3)
#Display the image
cv2.imshow("img",img)

cv2.waitKey(0)

