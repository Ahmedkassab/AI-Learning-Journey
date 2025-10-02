print("AI")
import numpy as np
grades_input = input()
grades = [float(grade) for grade in grades_input.split(',') ]
average_grade = np.mean(grades)
print(f'average grade: {average_grade:.2f}')
prices = [200000, 2500029.99, 800004.99, 49.99]
normalized_prices = (prices - np.min(prices)) / (np.max(prices) - np.min(prices))
print(f'normalized prices: {normalized_prices}')
print("another way to write the code")
grades = []
while True:
    user_input = input("Enter agrade :or 'done' to finish.")
    if user_input.lower() == "done":
        break
    try:
        grade = float(user_input) #convert user input to a number
        if 0<= grade <=100:
            grades.append(grade)
        else:
            print("Invalid grade. Please enter a number between 0 and 100.")
    except ValueError:
        print("Invalid input! Enter a number or 'done'.")
if grades: #check if grades list is not empty
    total = sum(grades)
    count = len(grades)
    average = total/count
    print(f"Average grade:{average:.2f}")
    max_grade = max(grades)
    min_grade = min(grades)
    print(f"Max grade: {max_grade}")
    print(f"Min grade: {min_grade}")
else:
    print("No grades were entered.")
               