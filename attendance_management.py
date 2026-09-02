import json
from datetime import date, datetime
from pathlib import Path

DATA_FILE = Path("attendance_data.json")
STATUSES = {"P": "Present", "A": "Absent", "L": "Late"}


def load_data():
    if not DATA_FILE.exists():
        return {"students": {}, "attendance": {}}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            data.setdefault("students", {})
            data.setdefault("attendance", {})
            return data
    except (json.JSONDecodeError, OSError):
        print("Could not read attendance_data.json. Starting fresh.")
        return {"students": {}, "attendance": {}}


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def ask_date():
    while True:
        value = input("Date YYYY-MM-DD (blank for today): ").strip()
        if not value:
            return date.today().isoformat()
        try:
            return datetime.strptime(value, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("Invalid date format.")


def add_student(data):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    student_id = str(max([int(key) for key in data["students"] if key.isdigit()] or [0]) + 1).zfill(3)
    data["students"][student_id] = name
    save_data(data)
    print(f"Added {name} with ID {student_id}.")


def list_students(data):
    if not data["students"]:
        print("No students found.")
        return
    print("\nID     Student")
    print("--------------")
    for student_id, name in sorted(data["students"].items()):
        print(f"{student_id:<6} {name}")


def mark_attendance(data):
    if not data["students"]:
        print("Add students first.")
        return
    attendance_date = ask_date()
    records = data["attendance"].setdefault(attendance_date, {})
    print("Enter P = Present, A = Absent, L = Late")
    for student_id, name in sorted(data["students"].items()):
        while True:
            status = input(f"{student_id} - {name}: ").strip().upper()
            if status in STATUSES:
                records[student_id] = status
                break
            print("Please enter P, A, or L.")
    save_data(data)
    print("Attendance saved.")


def daily_report(data):
    attendance_date = ask_date()
    records = data["attendance"].get(attendance_date, {})
    if not records:
        print("No attendance recorded for this date.")
        return
    print(f"\nAttendance for {attendance_date}")
    for student_id, name in sorted(data["students"].items()):
        status = STATUSES.get(records.get(student_id), "Not marked")
        print(f"{student_id} - {name}: {status}")


def student_summary(data):
    list_students(data)
    student_id = input("Student ID: ").strip()
    if student_id not in data["students"]:
        print("Student not found.")
        return
    counts = {status: 0 for status in STATUSES}
    for records in data["attendance"].values():
        status = records.get(student_id)
        if status in counts:
            counts[status] += 1
    total = sum(counts.values())
    rate = counts["P"] / total * 100 if total else 0
    print(f"\nSummary for {data['students'][student_id]}")
    print(f"Present: {counts['P']}")
    print(f"Absent:  {counts['A']}")
    print(f"Late:    {counts['L']}")
    print(f"Attendance rate: {rate:.1f}%")


def remove_student(data):
    list_students(data)
    student_id = input("Student ID to remove: ").strip()
    if student_id not in data["students"]:
        print("Student not found.")
        return
    name = data["students"].pop(student_id)
    for records in data["attendance"].values():
        records.pop(student_id, None)
    save_data(data)
    print(f"Removed {name}.")


def main():
    data = load_data()
    while True:
        print("\n=== Attendance Management System ===")
        print("1. Add student")
        print("2. List students")
        print("3. Mark attendance")
        print("4. Daily report")
        print("5. Student summary")
        print("6. Remove student")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(data)
        elif choice == "2":
            list_students(data)
        elif choice == "3":
            mark_attendance(data)
        elif choice == "4":
            daily_report(data)
        elif choice == "5":
            student_summary(data)
        elif choice == "6":
            remove_student(data)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
