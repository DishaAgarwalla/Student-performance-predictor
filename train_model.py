import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("data.csv")

# Features and Target
X = data[['study_hours', 'attendance', 'previous_marks']]
y = data['final_score']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 1️⃣ Linear Regression Model
# -------------------------------
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)
lr_accuracy = r2_score(y_test, lr_predictions)

print("Linear Regression Accuracy:", round(lr_accuracy * 100, 2), "%")

# -------------------------------
# 2️⃣ Random Forest Model
# -------------------------------
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)
rf_accuracy = r2_score(y_test, rf_predictions)

print("Random Forest Accuracy:", round(rf_accuracy * 100, 2), "%")

# -------------------------------
# 🏆 Choose Best Model
# -------------------------------
if rf_accuracy > lr_accuracy:
    best_model = rf_model
    best_accuracy = rf_accuracy
    best_model_name = "Random Forest"
else:
    best_model = lr_model
    best_accuracy = lr_accuracy
    best_model_name = "Linear Regression"

print("\nBest Model Selected:", best_model_name)
print("Best Model Accuracy:", round(best_accuracy * 100, 2), "%")

# Save best model
pickle.dump(best_model, open("model.pkl", "wb"))

print("\nModel saved as model.pkl")
