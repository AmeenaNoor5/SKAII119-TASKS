import cv2

# Ensure this path is correct
# If the file is in the same directory as this script, use just the file name
cascade_path = 'C:/Users/user/Desktop/TASK2/haarcascade_frontalface_default.xml'

# Load the pre-trained Haarcascade XML file for face detection
cascade_face = cv2.CascadeClassifier(cascade_path)

# Check if the cascade file was loaded correctly
if cascade_face.empty():
    raise IOError(f"Cannot open '{cascade_path}'. Please ensure the file exists and the path is correct.")

# Start video capture from the default camera (0)
cap = cv2.VideoCapture(0)

# Continuously capture frames from the camera
while True:
    # Read a frame from the camera
    ret, img = cap.read()
    
    # Print whether the frame was successfully captured
    print(ret)
    
    # Convert the frame to grayscale (face detection works better on grayscale images)
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    f = cascade_face.detectMultiScale(g, 1.3, 4)
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in f:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
    
    # Display the frame with detected faces
    cv2.imshow('img', img)
    
    # Wait for 30 ms and check if the 'Esc' key is pressed (ASCII code 27)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
