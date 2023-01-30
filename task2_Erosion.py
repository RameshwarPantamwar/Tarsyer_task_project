import cv2
import numpy as np

img = cv2.imread("j.png")
kernel = np.ones((5, 5), np.uint8)
image_erode = cv2.erode(img, kernel)
filename = 'j_erosion.png'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, image_erode)
