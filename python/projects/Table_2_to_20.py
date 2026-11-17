import os

# Create a folder named "tables"
os.makedirs("tables", exist_ok=True)

# Generate tables from 2 to 20
for i in range(2, 21):

    # Create a separate file for each table
    with open(f"tables/table_{i}.txt", "w") as f:

        # Write the multiplication table
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")

print("Multiplication tables from 2 to 20 have been created!")