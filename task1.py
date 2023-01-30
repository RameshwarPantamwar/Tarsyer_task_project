import cv2

# Load the image
img = cv2.imread("Task_1.jpg")

# Show the image to the user
cv2.imshow("Task 1", img)

# Wait for the user to select the crop area
r = cv2.selectROI(img)

# Crop the image
cropped_img = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# Save the cropped image
cv2.imwrite("Task_1_cropped.jpg", cropped_img)

# Draw the rectangular box on the original image
cv2.rectangle(img, (int(r[0]), int(r[1])), (int(r[0]+r[2]), int(r[1]+r[3])), (0, 0, 255), 2)

# Add text to indicate top-left and bottom-right points
cv2.putText(img, f"Top-left: ({int(r[0])}, {int(r[1])})", (int(r[0]), int(r[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
cv2.putText(img, f"Bottom-right: ({int(r[0]+r[2])}, {int(r[1]+r[3])})", (int(r[0]+r[2]), int(r[1]+r[3])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# Save the annotated image
cv2.imwrite("Task_1_insights.jpg", img)

# Close the window
cv2.destroyAllWindows()
