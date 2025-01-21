## Code starts from here for non website part
# import cv2
# import numpy as np
# import os
# import csv

# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('trainer/trainer.yml')  # Make sure this file exists
# cascadePath = r"C:\Users\naras\Downloads\Facial-Recognition-Attendance-system-master\Cascades\haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascadePath)

# font = cv2.FONT_HERSHEY_SIMPLEX  # Font type

# # Initialize id counter
# id = 0

# # Names related to ids: example ==> Ria: id=1, etc
# names = ['None', 'Narasimha', 'Ram Nag', 'Dhruv']

# # Initialize and start realtime video capture
# cam = cv2.VideoCapture(0)
# cam.set(3, 640)  # Set video width
# cam.set(4, 480)  # Set video height

# # Define min window size to be recognized as a face
# minW = 0.1 * cam.get(3)
# minH = 0.1 * cam.get(4)

# # Initialize attendance data
# attendance_data = set()  # Use set to avoid duplicates

# while True:
#     ret, img = cam.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.2,
#         minNeighbors=5,
#         minSize=(int(minW), int(minH)),
#     )

#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

#         # Check if confidence is less than 100 ==> "0" is perfect match
#         if confidence < 100:
#             id = names[id]
#             confidence = f"  {round(100 - confidence)}%"
#         else:
#             id = "None"
#             confidence = f"  {round(100 - confidence)}%"

#         cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
#         cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

#         if id != "None":  # Only add recognized faces to attendance
#             attendance_data.add((id, names.index(id)))

#     cv2.imshow('camera', img)

#     k = cv2.waitKey(10) & 0xFF  # Press 'ESC' for exiting video
#     if k == 27:  # ESC key
#         break
#     elif k == ord('q'):  # Press 'q' key to exit the camera
#         print("[INFO] Camera turned off.")
#         break

# # Write the attendance data to CSV files
# print("\n [INFO] Saving attendance data.")
# with open('attendance.csv', 'a', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerow(['Person', 'ID'])
#     for entry in attendance_data:
#         writer.writerow([entry[0], entry[1]])

# # Remove duplicates and save final attendance
# with open('attendance.csv', 'r') as f:
#     rows = f.readlines()

# rows = list(dict.fromkeys(rows))  # Remove duplicates
# with open('FinalAttendance.csv', 'w') as f:
#     f.writelines(rows)

# # Do a bit of cleanup
# print("\n [INFO] Exiting Program and cleanup.")
# cam.release()
# cv2.destroyAllWindows()




# Code starts from here for website
import cv2
import csv
import os

def start_recognition():
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    recognizer.read('trainer/trainer.yml')
    cascadePath = r"C:\Users\naras\Downloads\Facial-Recognition-Attendance-system-master\Cascades\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    names = ['None', 'Narasimha', 'Ram Nag', 'Pragnesh', 'Dhruv']
    attendance_data = set()

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not access the camera.")
        return

    cam.set(3, 640)
    cam.set(4, 480)
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            if confidence < 100:
                id = names[id]
                confidence_text = f"{100 - confidence:.2f}%"
                attendance_data.add((id, names.index(id)))

                # Draw a rectangle around the face
                color = (0, 255, 0)  # Green color for rectangle
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

                # Display the name and confidence
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(
                    img,
                    f"{id}, {confidence_text}",
                    (x, y - 10),
                    font,
                    0.6,
                    color,
                    2
                )
            else:
                id = "Unknown"
                confidence_text = f"{100 - confidence:.2f}%"

                # Draw rectangle for unknown face
                color = (0, 0, 255)  # Red color for rectangle
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

                # Display "Unknown"
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(
                    img,
                    f"{id}, {confidence_text}",
                    (x, y - 10),
                    font,
                    0.6,
                    color,
                    2
                )

        # Display the image with detected face(s)
        cv2.imshow("Face Recognition", img)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):  # 'q' to exit
            print("Exiting face recognition.")
            break

    cam.release()
    cv2.destroyAllWindows()

    # Save attendance
    with open('attendance.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Person', 'ID'])
        for entry in attendance_data:
            writer.writerow(entry)

    # Ensure there are no duplicates
    with open('attendance.csv', 'r') as f:
        rows = f.readlines()
    rows = list(dict.fromkeys(rows))  # Remove duplicate rows
    with open('FinalAttendance.csv', 'w') as f:
        f.writelines(rows)
