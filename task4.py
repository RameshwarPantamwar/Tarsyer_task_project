import cv2
import numpy as np

# Load a pre-trained hand detection model
model = cv2.CascadeClassifier("hand.xml")

# Dictionary to map finger names to alphabets
fingers = {0: "T", 1: "I", 2: "M", 3: "R", 4: "B"}

# Initialize webcam capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hands in the frame
    hands = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around each hand
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop the hand region
        roi = gray[y:y + h, x:x + w]

        # Count the number of raised fingers
        count = 0
        for i in range(0, h, h//5):
            if np.count_nonzero(roi[i:i + h//5, w//2:]) >= w//10:
                count += 1

        # Display the corresponding alphabet
        if count > 0:
            cv2.putText(frame, fingers[count-1], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the output frame
    cv2.imshow("Hand Tracking", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
