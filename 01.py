# A simple program to greet the user and check their age

# Get user input
name = input("What's your name? ")
age = int(input("How old are you? "))

# Print a greeting
print(f"Hello, {name}!")

# Simple conditional check
if age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
else:
    print("You are an adult!")