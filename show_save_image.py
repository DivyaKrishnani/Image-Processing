
import numpy as np
import cv2

img2 = cv2.imread('1.jpg', 0)
cv2.imshow('IMAGE', img2)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('copy1.png', img2)
    cv2.destroyAllWindows()
