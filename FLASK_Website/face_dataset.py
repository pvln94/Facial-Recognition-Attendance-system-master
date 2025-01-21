import cv2
import os

# Initialize camera
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set video width
cam.set(4, 480)  # Set video height

# Load the face detection model
face_detector = cv2.CascadeClassifier(r"C:\Users\naras\Downloads\Facial-Recognition-Attendance-system-master\Cascades\haarcascade_frontalface_default.xml")

# Input user ID
face_id = input('\nEnter user ID and press <return> ==> ')

print("\n[INFO] Initializing face capture. Look at the camera and wait...")

# Initialize individual sampling face count
count = 0

# Ensure the dataset directory exists
os.makedirs('dataset', exist_ok=True)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  
        count += 1

        # Save the captured image into the dataset folder
        cv2.imwrite(f"dataset/User.{str(face_id)}.{str(count)}.jpg", gray[y:y + h, x:x + w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:  # ESC key to break
        break
    elif count >= 100:  # Take 100 face samples and stop
        break

# Cleanup
print("\n[INFO] Exiting program and cleanup.")
cam.release()
cv2.destroyAllWindows()
