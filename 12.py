# Read and display student records from 'students.txt'


print("Reading contents of 'students.txt':")
with open("students.txt", "r") as file:
    content = file.read()
    print(content.strip())