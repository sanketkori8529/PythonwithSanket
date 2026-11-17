# Write student records to a text file


records = [
    "101, Student_A, CSE, 88\n",
    "102, Student_B, CSE, 92\n",
    "103, Student_C, CSE, 79\n"
]
with open("students.txt", "w") as file:
    file.write("RollNo, Name, Branch, Marks\n")
    file.writelines(records)
print("Student records written to 'students.txt' successfully.")