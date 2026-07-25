"""
=========================================================
                 PYTHON MASTER HUB
=========================================================

A single project to practice Python concepts:

1. Calculator
2. Number Guessing Game
3. Quiz Game
4. To-Do List
5. Contact Book
6. Student Manager
7. Expense Tracker
8. Password Generator
9. Notes
10. Multiplication Table
11. Number Analysis
12. Exit

Concepts used:
- Variables
- Input / Output
- Data Types
- Type Conversion
- Operators
- if / elif / else
- for loops
- while loops
- Lists
- Dictionaries
- Tuples
- Functions
- Modules
- File Handling
- Exception Handling

=========================================================
"""

import random
import string
import os


# =======================================================
#                 HELPER FUNCTIONS
# =======================================================

def pause():
    input("\nPress Enter to continue...")


def line():
    print("=" * 55)


# =======================================================
#                    CALCULATOR
# =======================================================

def calculator():

    while True:

        line()
        print("                 CALCULATOR")
        line()

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue

        try:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2

            elif choice == "2":
                result = num1 - num2

            elif choice == "3":
                result = num1 * num2

            elif choice == "4":

                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue

                result = num1 / num2

            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers.")


# =======================================================
#                NUMBER GUESSING GAME
# =======================================================

def guessing_game():

    line()
    print("              NUMBER GUESSING GAME")
    line()

    secret_number = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100.")

    while True:

        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")

            elif guess > secret_number:
                print("Too high!")

            else:
                print("\nCongratulations!")
                print("You guessed the number in", attempts, "attempts.")
                break

        except ValueError:
            print("Enter a valid number.")


# =======================================================
#                     QUIZ GAME
# =======================================================

def quiz_game():

    questions = {
        "What is the capital of India?": "delhi",
        "Which language are you learning?": "python",
        "What is 5 + 5?": "10",
        "What keyword is used to define a function?": "def"
    }

    score = 0

    line()
    print("                    QUIZ")
    line()

    for question, answer in questions.items():

        print("\nQuestion:", question)

        user_answer = input("Your answer: ")

        if user_answer.lower() == answer:
            print("Correct!")
            score += 1

        else:
            print("Wrong!")
            print("Correct answer:", answer)

    print("\nYour final score:", score, "/", len(questions))


# =======================================================
#                     TO-DO LIST
# =======================================================

def todo_list():

    tasks = []

    while True:

        line()
        print("                  TO-DO LIST")
        line()

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            task = input("Enter task: ")

            tasks.append(task)

            print("Task added successfully!")

        elif choice == "2":

            if len(tasks) == 0:

                print("No tasks found.")

            else:

                print("\nYour Tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(number, ".", task)

        elif choice == "3":

            if len(tasks) == 0:

                print("No tasks to delete.")

            else:

                for number, task in enumerate(tasks, start=1):
                    print(number, ".", task)

                try:

                    number = int(input("Enter task number: "))

                    if 1 <= number <= len(tasks):

                        removed = tasks.pop(number - 1)

                        print(removed, "deleted.")

                    else:

                        print("Invalid task number.")

                except ValueError:

                    print("Enter a valid number.")

        elif choice == "4":

            break

        else:

            print("Invalid choice!")


# =======================================================
#                    CONTACT BOOK
# =======================================================

def contact_book():

    contacts = {}

    while True:

        line()
        print("                 CONTACT BOOK")
        line()

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            name = input("Enter name: ")
            phone = input("Enter phone number: ")

            contacts[name] = phone

            print("Contact saved!")

        elif choice == "2":

            if len(contacts) == 0:

                print("No contacts found.")

            else:

                for name, phone in contacts.items():

                    print(name, ":", phone)

        elif choice == "3":

            name = input("Enter name to search: ")

            if name in contacts:

                print("Phone:", contacts[name])

            else:

                print("Contact not found.")

        elif choice == "4":

            name = input("Enter name to delete: ")

            if name in contacts:

                del contacts[name]

                print("Contact deleted.")

            else:

                print("Contact not found.")

        elif choice == "5":

            break

        else:

            print("Invalid choice!")


# =======================================================
#                  STUDENT MANAGER
# =======================================================

def student_manager():

    students = {}

    while True:

        line()
        print("               STUDENT MANAGER")
        line()

        print("1. Add Student")
        print("2. View Students")
        print("3. Find Top Student")
        print("4. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            name = input("Enter student name: ")

            try:

                marks = float(input("Enter marks: "))

                if 0 <= marks <= 100:

                    students[name] = marks

                    print("Student added!")

                else:

                    print("Marks must be between 0 and 100.")

            except ValueError:

                print("Enter valid marks.")

        elif choice == "2":

            if len(students) == 0:

                print("No students found.")

            else:

                for name, marks in students.items():

                    print(name, ":", marks)

        elif choice == "3":

            if len(students) == 0:

                print("No student data available.")

            else:

                top_student = max(students, key=students.get)

                print("Top Student:", top_student)
                print("Marks:", students[top_student])

        elif choice == "4":

            break

        else:

            print("Invalid choice!")


# =======================================================
#                   EXPENSE TRACKER
# =======================================================

def expense_tracker():

    expenses = []

    while True:

        line()
        print("                EXPENSE TRACKER")
        line()

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            name = input("Enter expense name: ")

            try:

                amount = float(input("Enter amount (£): "))

                expenses.append((name, amount))

                print("Expense added!")

            except ValueError:

                print("Enter a valid amount.")

        elif choice == "2":

            if len(expenses) == 0:

                print("No expenses found.")

            else:

                for name, amount in expenses:

                    print(name, ":", "£", amount)

        elif choice == "3":

            total = 0

            for name, amount in expenses:

                total += amount

            print("Total expenses: £", total)

        elif choice == "4":

            break

        else:

            print("Invalid choice!")


# =======================================================
#                PASSWORD GENERATOR
# =======================================================

def password_generator():

    line()
    print("              PASSWORD GENERATOR")
    line()

    try:

        length = int(input("Enter password length: "))

        if length <= 0:

            print("Length must be greater than 0.")
            return

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = ""

        for i in range(length):

            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

    except ValueError:

        print("Enter a valid number.")


# =======================================================
#                     NOTES APP
# =======================================================

def notes_app():

    while True:

        line()
        print("                   NOTES")
        line()

        print("1. Write Note")
        print("2. Read Notes")
        print("3. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            note = input("Write your note: ")

            with open("notes.txt", "a") as file:

                file.write(note + "\n")

            print("Note saved!")

        elif choice == "2":

            if os.path.exists("notes.txt"):

                with open("notes.txt", "r") as file:

                    content = file.read()

                print("\nYour Notes:")
                print(content)

            else:

                print("No notes found.")

        elif choice == "3":

            break

        else:

            print("Invalid choice!")


# =======================================================
#               MULTIPLICATION TABLE
# =======================================================

def multiplication_table():

    try:

        number = int(input("Enter number: "))

        for i in range(1, 11):

            print(number, "x", i, "=", number * i)

    except ValueError:

        print("Enter a valid number.")


# =======================================================
#                  NUMBER ANALYSIS
# =======================================================

def number_analysis():

    try:

        number = int(input("Enter a number: "))

        print("\nNumber:", number)

        if number % 2 == 0:

            print("Type: Even")

        else:

            print("Type: Odd")

        if number > 0:

            print("Sign: Positive")

        elif number < 0:

            print("Sign: Negative")

        else:

            print("Sign: Zero")

    except ValueError:

        print("Enter a valid integer.")


# =======================================================
#                   MAIN MENU
# =======================================================

def main():

    while True:

        print("\n")

        line()

        print("              PYTHON MASTER HUB")

        line()

        print("1. Calculator")
        print("2. Number Guessing Game")
        print("3. Quiz Game")
        print("4. To-Do List")
        print("5. Contact Book")
        print("6. Student Manager")
        print("7. Expense Tracker")
        print("8. Password Generator")
        print("9. Notes App")
        print("10. Multiplication Table")
        print("11. Number Analysis")
        print("12. Exit")

        line()

        choice = input("Enter your choice: ")

        if choice == "1":

            calculator()

        elif choice == "2":

            guessing_game()

        elif choice == "3":

            quiz_game()

        elif choice == "4":

            todo_list()

        elif choice == "5":

            contact_book()

        elif choice == "6":

            student_manager()

        elif choice == "7":

            expense_tracker()

        elif choice == "8":

            password_generator()

        elif choice == "9":

            notes_app()

        elif choice == "10":

            multiplication_table()

        elif choice == "11":

            number_analysis()

        elif choice == "12":

            print("\nThank you for using Python Master Hub!")
            print("Keep learning Python!")
            break

        else:

            print("\nInvalid choice. Please try again.")


# =======================================================
#                 START PROGRAM
# =======================================================

main()