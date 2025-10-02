print("AI")
import numpy as np
grades = [85, 90, 78, 92, 88]
average_grade = np.mean(grades)
print(f'average grade: {average_grade:.2f}')
prices = [200000, 2500029.99, 800004.99, 49.99]
normalized_prices = (prices - np.min(prices)) / (np.max(prices) - np.min(prices))
print(f'normalized prices: {normalized_prices}')