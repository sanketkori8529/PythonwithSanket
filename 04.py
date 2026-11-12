# Temperature converter (°C ↔ °F) 

choice = input("Convert from (C/F): ").strip().upper()
if choice == 'C':
    c = float(input("Enter temperature in Celsius (°C): "))
    f = (c * 9 / 5) + 32
    print(f"{c:.2f} °C = {f:.2f} °F")
elif choice == 'F':
    f = float(input("Enter temperature in Fahrenheit (°F): "))
    c = (f - 32) * 5 / 9
    print(f"{f:.2f} °F = {c:.2f} °C")
else:
    print("Invalid selection.")