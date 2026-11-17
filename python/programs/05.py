#  Grade calculator in Python.

marks = float(input("Enter marks (0 - 100): "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"
print(f"Marks: {marks:.1f} -> Grade: {grade}")