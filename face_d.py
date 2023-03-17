import cv2
import os

# Create a directory to store the detected faces
if not os.path.exists('data'):
    os.makedirs('data')

# Load the pre-trained face detector
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_id = input('\n enter user id end press <return> ==>  ')
# Open the camera
count=0
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))

    # Draw a rectangle around each detected face and save it to the 'detected_faces' directory
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count+=1
        face_image = frame[y:y+h, x:x+w]
        cv2.imwrite("data/" + str(face_id) + '.' + ".jpg", face_image)

    # Display the resulting image
    cv2.imshow('Face Detection', frame)

    # Exit if the 'q' key is pressed
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 10:
         break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
