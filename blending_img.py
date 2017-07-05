import numpy as np
import cv2

#Both images to be of same size
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

img = cv2.addWeighted(img1,0.4,img2,0.6,0)

cv2.imshow('Blended',img)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('blended2.png', dst)
    cv2.destroyAllWindows()
