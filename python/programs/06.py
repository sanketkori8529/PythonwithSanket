# Fibonacci using Python loop.

n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()