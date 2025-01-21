import cv2
import numpy as np
from PIL import Image
import os

# Path for the face image database
path = r"C:\Users\naras\Downloads\Facial-Recognition-Attendance-system-master\dataset"

# Initialize the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the Haar Cascade for face detection
detector = cv2.CascadeClassifier(r"C:\Users\naras\Downloads\Facial-Recognition-Attendance-system-master\Cascades\haarcascade_frontalface_default.xml")

# Function to get images and labels
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(('jpg', 'jpeg', 'png'))]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')

        try:
            id = int(os.path.split(imagePath)[-1].split(".")[1])
        except ValueError:
            print(f"[WARNING] Skipping invalid file: {imagePath}")
            continue

        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)

    return faceSamples, ids

# Train the model
print("\n[INFO] Training faces. It will take a few seconds. Please wait...")

faces, ids = getImagesAndLabels(path)

if faces and ids:
    recognizer.train(faces, np.array(ids))

    # Save the trained model into trainer/trainer.yml
    os.makedirs('trainer', exist_ok=True)  # Ensure the trainer folder exists
    recognizer.write('trainer/trainer.yml')  # Save the trained model

    print(f"\n[INFO] {len(np.unique(ids))} faces trained. Exiting program.")
else:
    print("\n[ERROR] No faces found to train. Please check your dataset.")
