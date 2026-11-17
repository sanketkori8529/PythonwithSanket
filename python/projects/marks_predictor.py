import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# 1. Create a Sample Dataset (In real projects, you load this via pd.read_csv('data.csv'))
data = {
    "Study_Hours": [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0],
    "Attendance_Pct": [60, 65, 70, 72, 75, 78, 80, 85, 88, 90, 92, 96],
    "Previous_Score": [45, 50, 52, 58, 62, 65, 70, 74, 78, 82, 88, 94],
    "Final_Marks": [48, 52, 55, 60, 64, 68, 73, 77, 81, 85, 90, 96],
}

df = pd.DataFrame(data)

# 2. Separate Features (Inputs = X) and Target (Output = y)
X = df[["Study_Hours", "Attendance_Pct", "Previous_Score"]]
y = df["Final_Marks"]

# 3. Split Data: 80% for Training the AI, 20% for Testing its accuracy
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Initialize and Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate Model Performance on Unseen Test Data
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
accuracy = r2_score(y_test, predictions)

print("=== MODEL EVALUATION ===")
print(f"Mean Absolute Error: ±{mae:.2f} marks")
print(f"R² Score (Accuracy): {accuracy * 100:.2f}%\n")

# 6. Interactive Prediction for a New Student
print("=== PREDICT YOUR SEMESTER MARKS ===")
try:
  hours = float(input("Enter daily study hours (e.g., 4.5): "))
  attendance = float(input("Enter attendance percentage (e.g., 82): "))
  prev_score = float(input("Enter previous exam marks out of 100 (e.g., 70): "))

  # Format input as a DataFrame matching the training column names
  new_student = pd.DataFrame(
      [[hours, attendance, prev_score]],
      columns=["Study_Hours", "Attendance_Pct", "Previous_Score"],
  )

  predicted_marks = model.predict(new_student)[0]

  # Cap the score between 0 and 100
  predicted_marks = max(0, min(100, predicted_marks))
  print(f"\n🎯 Predicted Final Exam Score: {predicted_marks:.2f} / 100")

except ValueError:
  print("Please enter valid numeric values.")