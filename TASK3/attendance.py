import cv2
import openpyxl
from openpyxl import Workbook
import os

# Path to the Haarcascade XML file for face detection
cascade_path = 'haarcascade_frontalface_default.xml'

# Load the pre-trained Haarcascade XML file for face detection
cascade_face = cv2.CascadeClassifier(cascade_path)

# Start video capture from the default camera (0)
cap = cv2.VideoCapture(0)

# Create or load the workbook
xl_file = 'attendance.xlsx'
if os.path.exists(xl_file):
    wb = openpyxl.load_workbook(xl_file)
else:
    wb = Workbook()

# Select active sheet
sheet = wb.active

# Set column names
sheet['A1'] = 'ID'
sheet['B1'] = 'Attendance'

# Initialize row counter
row = 2

# Prompt user to enter ID
user_id = input("Enter your ID: ")

# Continuously capture frames from the camera
while True:
    # Read a frame from the camera
    ret, img = cap.read()
    
    # Convert the frame to grayscale (face detection works better on grayscale images)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = cascade_face.detectMultiScale(gray, 1.3, 4)
    
    # Record attendance for each recognized face
    for (x, y, w, h) in faces:
        # Extract face region from the grayscale image
        face_region = gray[y:y+h, x:x+w]
        
        # Recognize the face (you may use face recognition algorithms here)
        # For simplicity, let's just use the face coordinates as the identifier
        face_id = f"{x}-{y}-{w}-{h}"
        
        # Record attendance if the face is not already recognized
        if face_id not in [sheet[f'A{i}'].value for i in range(2, row)]:
            sheet[f'A{row}'] = user_id
            sheet[f'B{row}'] = 'Present'
            row += 1
    
    # Display the frame with detected faces
    cv2.imshow('Face Attendance System', img)
    
    # Wait for 30 ms and check if the 'Esc' key is pressed (ASCII code 27)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Save the workbook
wb.save(xl_file)

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
