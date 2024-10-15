import cv2
import os
import numpy as np  # Import NumPy

# Get the absolute path of the current script's directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load the Haarcascade file using the absolute path
faceCascade = cv2.CascadeClassifier(os.path.join(base_dir, 'haarcascade_frontalface_default.xml'))

# Check if the cascade file was loaded correctly
if faceCascade.empty():
    print("Failed to load cascade classifier")
    exit(1)

# Start video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Detect faces
    faces = faceCascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        
        # Extract face and convert to HSV
        face_roi = cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2HSV)
        
        # Skin tone range and mask
        mask = cv2.inRange(face_roi, np.array([0, 20, 70], np.uint8), np.array([20, 255, 255], np.uint8))
        
        # Apply mask
        skin = cv2.bitwise_and(frame[y:y + h, x:x + w], frame[y:y + h, x:x + w], mask=mask)
        cv2.imshow("Skin Detection", skin)

    # Show result
    cv2.imshow('Face Detection and Skin Segmentation', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
