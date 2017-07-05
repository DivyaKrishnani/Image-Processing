import cv2
import numpy as np


img= cv2.imread('2.jpg')

"""
cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming. By default, interpolation method used is cv2.INTER_LINEAR for all resizing purposes.
"""
res = cv2.resize(img,None,fx=0.75, fy=0.75, interpolation = cv2.INTER_LINEAR)


cv2.imshow('IMAGE', res)

k = cv2.waitKey(0) & 0xFF
if k == 27:      #for escape
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('copy.png', img2)
    cv2.destroyAllWindows()
