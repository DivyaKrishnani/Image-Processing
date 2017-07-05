import numpy as np
import cv2

# Create a white image
img = np.ones((512,512,3), np.uint8) * 255

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.ellipse(img,(200,200),(80,50),0,0,360,(0,255,0),-1)
cv2.ellipse(img,(200,200),(80,50),45,0,360,(0,0,255),1)

cv2.imshow("img",img)

cv2.waitKey(0)
