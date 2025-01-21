# Facial Recognition Attendance System

This project uses facial recognition technology to mark attendance for individuals by detecting faces through a webcam. It stores the attendance records in CSV files, both with duplicates and without duplicates. The project consists of three main Python files: `face_dataset.py`, `face_training.py`, and `face_recognition.py`.

## Project Overview

When a person's face is recognized by the camera, their attendance will be recorded along with their name and ID in the attendance CSV file. If the face is not recognized, no changes will be made, and the face will be detected as "unknown." The project captures facial data, trains a recognition model, and marks attendance through a simple user interface or directly from the command line.

## Features

- **Face Dataset Collection:** Captures multiple images of a person to add to the dataset.
- **Face Training:** Trains a model on the captured images to recognize faces.
- **Attendance Tracking:** Automatically tracks and records attendance in two CSV files.
- **Flask Web Interface:** Provides a simple webpage to view live attendance data and download records.

---

## Setup Instructions

To run this project on your local machine, follow the steps below:

### Step 1: Modify `face_recognition.py`

1. Open the `face_recognition.py` file.
2. Locate the `names` array, which holds the list of registered individuals. 
3. Add your name to the array. Your ID will correspond to your position in the array (starting from 0).

### Step 2: Run `face_dataset.py`

1. Run `face_dataset.py`. The program will prompt you to input your ID (the one you assigned to yourself in Step 1).
2. The program will use your webcam to capture multiple images of your face and store them in the dataset folder for future training.

### Step 3: Run `face_training.py`

1. Run `face_training.py` to train the facial recognition model.
2. This will generate a `trainer.yml` file that contains the trained data.

### Step 4: Run `face_recognition.py`

1. Run `face_recognition.py`. 
2. The program will start recognizing faces and recording attendance in two CSV files:
   - **`attendance.csv`**: Contains records for each time a face is detected (with potential duplicates).
   - **`FinalAttendance.csv`**: Contains the final list of unique records without duplicates.

---

## Demo

### Attendance System
Once a person is recognized, their attendance will be automatically marked in the `attendance.csv` file, with their respective name and ID.

![image](https://github.com/user-attachments/assets/487b326b-94d8-4c60-b2b8-4c693c411dce)

![image](https://github.com/user-attachments/assets/78b9ec10-8031-4bf1-9253-ffea55c117b3)
---

---
## Flask Web Interface
![image](https://github.com/user-attachments/assets/75455919-a7e8-40e2-bfc1-7f26b8566258)

### Workflow

Follow the same steps (1, 2, and 3) to capture images and train the model. Afterward, you can run the Flask web interface directly.

1. **Run `app.py`:** This starts the Flask web application.
2. The website will run on your local system at `http://127.0.0.1:5000`.

### Web Interface Features:
- View live attendance data.
- Download the latest attendance records as a CSV file.
![image](https://github.com/user-attachments/assets/f7ad0523-e0d0-4e26-be47-5c89b596f6b3)

![image](https://github.com/user-attachments/assets/858d7b3f-bdd8-4483-af14-db0de3e3bd7d)

![image](https://github.com/user-attachments/assets/52c2268b-d2c9-48a1-af46-472c6107734d)

You can view your attendance directly on the webpage and even download the live data as a CSV file.
![image](https://github.com/user-attachments/assets/3050cf8a-2b4e-4d80-a863-72c0142c4cc7)

Download live data:
![image](https://github.com/user-attachments/assets/78b9ec10-8031-4bf1-9253-ffea55c117b3)
---


