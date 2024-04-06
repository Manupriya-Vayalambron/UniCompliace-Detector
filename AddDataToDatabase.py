import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://attendance-system-7ad62-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
        {
            "last_attendance_time": "2024-2-17 02:10:30",
            "Name": "Abhijith Panicker",
            "Department": "Computer Science",
            "Semester": "S6",
            "total_attendance": 0,
            "year": 3
        },
    "8":
        {
            "last_attendance_time": "2024-2-17 02:10:30",
            "Name": "Arif Muhammad",
            "Department": "Computer Science",
            "Semester": "S6",
            "total_attendance": 0,
            "year": 3
        },
    "ayush":
        {
            "last_attendance_time": "2024-2-17 02:10:30",
            "Name": "Ayush Subhash",
            "Department": "Computer Science",
            "Semester": "S6",
            "total_attendance": 2,
            "year": 3
        },
    "13":
        {
            "last_attendance_time": "2024-2-17 02:10:30",
            "Name": "Krishna RS",
            "Department": "Computer Science",
            "Semester": "S5",
            "total_attendance": 0,
            "year": 3
        },
    "16":
        {
            "last_attendance_time": "2024-2-17 02:10:30",
            "Name": "Muneer M",
            "Department": "Computer Science",
            "Semester": "S6",
            "total_attendance": 5,
            "year": 3
        },
    "15":
        {
            "last_attendance_time": "2024-2-17 02:10:30",
            "Name": "Manupriya",
            "Department": "Computer Science",
            "Semester": "S6",
            "total_attendance": 5,
            "year": 3
        },
    "9":
        {
            "last_attendance_time": "2024-2-17 02:10:30",
            "Name": "Arun prekash R L",
            "Department": "Computer Science",
            "Semester": "S6",
            "total_attendance": 5,
            "year": 3
        }
}

for key,value in data.items():
    ref.child(key).set(value)