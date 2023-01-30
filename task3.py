import cv2
import numpy as np

img = cv2.imread("Task_3.jpg", 0)

# Simple Thresholding
_, simple_threshold = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
cv2.imwrite("Task_3_simple.jpg", simple_threshold)

# Adaptive Thresholding
adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite("Task_3_adaptive.jpg", adaptive_threshold)
