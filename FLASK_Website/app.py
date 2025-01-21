from flask import Flask, render_template, redirect, url_for, send_file
import csv
import os
from face_recognition import start_recognition

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the home page with navigation options.
    """
    return render_template('index.html')

@app.route('/start_recognition')
def start_recognition_route():
    """
    Start the face recognition process and redirect to the attendance page.
    """
    start_recognition()  # Call the face recognition function
    return redirect(url_for('attendance'))

@app.route('/attendance')
def attendance():
    """
    Display the attendance records by reading the FinalAttendance.csv file.
    """
    attendance_data = []
    if os.path.exists('FinalAttendance.csv'):
        try:
            with open('FinalAttendance.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                attendance_data = [row for row in reader]
        except Exception as e:
            print(f"Error reading attendance file: {e}")
    return render_template('attendance.html', attendance=attendance_data)

@app.route('/download_csv')
def download_csv():
    """
    Provide the attendance CSV file for download.
    """
    file_path = os.path.abspath('FinalAttendance.csv')  # Ensure absolute path is used
    if os.path.exists(file_path):
        try:
            return send_file(
                file_path,
                as_attachment=True,
                download_name='Attendance.csv',  # Updated for Flask 2.0+
                mimetype='text/csv'
            )
        except Exception as e:
            print(f"Error serving CSV file: {e}")
            return "Error downloading file.", 500
    else:
        print("Attendance file not found.")
        return "Attendance file not found.", 404


if __name__ == "__main__":
    app.run(debug=True)

