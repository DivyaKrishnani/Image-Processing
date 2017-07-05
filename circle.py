import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a red closed circle #To draw a circle, you need its center coordinates and radius.
cv2.circle(img,(200,200), 40, (0,0,255), -1)
cv2.circle(img,(447,63), 63, (0,255,255), -1)
#Display the image
cv2.imshow("img",img)

cv2.waitKey(0)
