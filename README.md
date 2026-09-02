# Python Learning Programs

This workspace contains beginner Python exercises and an attendance management program.

## Attendance Management System

The main program is [attendance_management.py](attendance_management.py). It is a simple command-line application for managing students and daily attendance.

### Run the program

Open a terminal in this folder and run:

```text
python attendance_management.py
```

### Features

1. Add a student and automatically generate an ID.
2. List all students.
3. Mark each student as Present, Absent, or Late.
4. View attendance for a selected date.
5. View a student's attendance summary and attendance rate.
6. Remove a student and their attendance records.
7. Exit the program.

### Data storage

The program automatically creates `attendance_data.json` after the first change. This file stores student and attendance information locally. Keep it in the same folder as `attendance_management.py`.

### Example workflow

1. Select `1` and add a student.
2. Select `3` and enter attendance using `P`, `A`, or `L`.
3. Select `4` to see the daily report.
4. Select `5` to see an individual student's summary.

Dates must use `YYYY-MM-DD`, for example `2026-09-03`. Press Enter without typing a date to use today's date.



Run any lesson like this:

```text
python python_beginner/01_hello.py
```
