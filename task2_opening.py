import numpy as np
import imutils
import cv2
#reading the input image
img = cv2.imread("j.png")
kernel = np.ones((5,5), dtype = "uint8")/9
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite('j_opening.jpg', opening)