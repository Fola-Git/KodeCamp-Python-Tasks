import json, os

DATA_FILE = "students.json"

class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects  # dict: {"Math": 90, "English": 80}

    def average(self):
        return sum(self.subjects.values()) / len(self.subjects)

    def grade(self):
        avg = self.average()
        if avg >= 70:
            return "A"
        elif avg >= 50:
            return "B"
        else:
            return "C"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_student():
    name = input("Enter name: ")
    subjects = {}
    for sub in ["Math", "English", "Science"]:
        score = int(input(f"Enter score for {sub}: "))
        subjects[sub] = score
    student = Student(name, subjects)
    data = load_data()
    data.append({"name": name, "subjects": subjects, "average": student.average(), "grade": student.grade()})
    save_data(data)
    print(f"Student {name} added!")

def view_students():
    data = load_data()
    for s in data:
        print(f"{s['name']} - Avg: {s['average']:.2f} - Grade: {s['grade']}")

# Simple menu
while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Choose: ")
    if choice == "1": add_student()
    elif choice == "2": view_students()
    else: break
