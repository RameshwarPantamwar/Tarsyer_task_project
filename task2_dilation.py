import cv2
import numpy as np

img = cv2.imread("j.png")
kernel = np.ones((5,5), np.uint8)
image_dilation = cv2.dilate(img, kernel, iterations=1)
filename = 'j_dilation.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, image_dilation)