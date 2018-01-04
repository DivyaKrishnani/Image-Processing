import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/dl4.crop.jpg')

    # Convert to gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.GaussianBlur(img,(3,3),0)
#img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
#ret,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # Apply dilation and erosion to remove some noise
"""
Mat imageMat = new Mat();
Utils.bitmapToMat(photo, imageMat);
Imgproc.cvtColor(imageMat, imageMat, Imgproc.COLOR_BGR2GRAY);
Imgproc.GaussianBlur(imageMat, imageMat, new Size(3, 3), 0);
Imgproc.adaptiveThreshold(imageMat, imageMat, 255, Imgproc.ADAPTIVE_THRESH_MEAN_C, Imgproc.THRESH_BINARY_INV, 5, 4);
"""
    # Write image after removed noise
    # cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
#img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
#ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret,img = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#kernel = np.ones((1,1), np.uint8)
#img = cv2.erode(img,kernel, iterations=1) #erosionimg = cv2.erode(img,kernel, iterations=1) #erosion
#img = cv2.dilate(img, kernel, iterations=3) #dilation
#img = cv2.dilate(img, kernel, iterations=3) #dilation
#img = cv2.erode(img,kernel, iterations=1)
#img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) #opening
#img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # switch it to rgb

# Denoising
#img = cv2.fastNlMeansDenoising(img,img,3,21,7)

#th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('IMAGE', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/dl4_g.jpg', img)
    cv2.destroyAllWindows()
