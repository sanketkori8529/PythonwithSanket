def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F (Fail)"

def add_student(students):
    print("\n--- ADD NEW STUDENT RECORD ---")
    roll_no = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()

    subjects = ["Mathematics", "Science", "English", "Social Studies", "Computer Science"]
    marks = {}

    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    total = sum(marks.values())
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    student_record = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }
    students.append(student_record)
    print(f"\nReport card generated for {name}!")

def display_all_reports(students):
    if not students:
        print("\nNo student records found.")
        return

    for s in students:
        print("\n============================================")
        print("            STUDENT REPORT CARD             ")
        print("============================================")
        print(f"Roll No   : {s['roll_no']}")
        print(f"Name      : {s['name']}")
        print("--------------------------------------------")
        for subject, score in s["marks"].items():
            print(f"{subject:<20}: {score:>6.2f} / 100")
        print("--------------------------------------------")
        print(f"Total Marks         : {s['total']:.2f} / 500")
        print(f"Percentage          : {s['percentage']:.2f}%")
        print(f"Grade               : {s['grade']}")
        print("============================================")

def search_student(students):
    roll_no = input("\nEnter Roll Number to search: ").strip()
    for s in students:
        if s["roll_no"] == roll_no:
            display_all_reports([s])
            return
    print("Student record not found.")

def main():
    students = []
    while True:
        print("\n=== STUDENT REPORT CARD SYSTEM ===")
        print("1. Add Student Marks & Generate Report")
        print("2. Display All Report Cards")
        print("3. Search Student by Roll Number")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_reports(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            print("\nExiting Report Card System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()