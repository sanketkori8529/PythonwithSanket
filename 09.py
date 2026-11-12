# Store and display name and marks of 3 students using a Dictionary


students = {
    "Student_1": 85,
    "Student_2": 91,
    "Student_3": 76
}
print("Student Records (Name : Marks):")
for name, score in students.items():
    print(f"  {name} : {score}")