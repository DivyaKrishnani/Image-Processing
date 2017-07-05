import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

# Draw a blue line with thickness of 5 px #To draw a line, you need to pass starting and ending coordinates of line.
cv2.line(img,(0,0),(511,511),(255,0,0),5)  #(BGR)

cv2.imshow("img",img)

cv2.waitKey(0)
