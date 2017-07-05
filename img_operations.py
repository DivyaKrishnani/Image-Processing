#Accessing and Modifying pixel values
import cv2
import numpy as np
import sys
imagepath=sys.argv[1]

img= cv2.imread(imagepath)

px=img[100,100]
print px

blue=img[100,100,0]
print blue

#########################################################################

print img.shape # tuple of number of rows, columns and channels (if color) if gray scale(only row and column)
print img.size  #Total pixels
print img.dtype   

#########################################################################

#Selecting a path and copyng to other region of the image
b=img[280:340, 330:390]
img[273:333, 100:160] =b
cv2.imshow('IMAGE', img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

##########################################################################
