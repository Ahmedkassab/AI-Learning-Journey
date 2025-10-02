import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data: house sizes (sqft) and prices
sizes = np.array([1400, 1600, 1700, 1875, 1100]).reshape(-1, 1)  # Feature
prices = np.array([245000, 312000, 279000, 308000, 199000])  # Target

# Train model
model = LinearRegression()
model.fit(sizes, prices)

# Predict price for a 1500 sqft house
predicted_price = model.predict([[1500]])
print(f"Predicted price for 1500 sqft: ${predicted_price[0]:.2f}")

# Plot data and regression line
plt.scatter(sizes, prices, color="blue", label="Data")
plt.plot(sizes, model.predict(sizes), color="red", label="Regression Line")
plt.xlabel("Size (sqft)")
plt.ylabel("Price ($)")
plt.legend()
plt.show()