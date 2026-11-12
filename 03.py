#BMI calculator

# BMI Calculator in Python
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25.0:
    print("Category: Normal weight")
elif bmi < 30.0:
    print("Category: Overweight")
else:
    print("Category: Obese")