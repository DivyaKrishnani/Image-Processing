import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Create a white image
#img = np.ones((512,512,3), np.uint8) * 255

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.ellipse(img,(200,200),(80,50),0,0,360,(0,255,0),-1)
cv2.ellipse(img,(200,200),(80,50),45,0,360,(0,0,255),1)

"""To draw the ellipse, we need to pass several arguments. One argument is the center location (x,y). Next argument is axes lengths (major axis length, minor axis length). angle is the angle of rotation of ellipse in anti-clockwise direction. startAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis. i.e. giving values 0 and 360 gives the full ellipse. """


#Display the image
cv2.imshow("img",img)

cv2.waitKey(0)
