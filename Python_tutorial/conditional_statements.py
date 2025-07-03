# # Program to check if a character is a vowel

# char = input("Enter a character: ")

# # Convert to lowercase for comparison
# char = char.lower()

# if char in ('a', 'e', 'i', 'o', 'u'):
#     print(char, "is a vowel.")
# else:
#     print(char, "is not a vowel.")



# # Program to classify a person's age group

# age = int(input("Enter your age: "))

# if 0 <= age <= 12:
#     print("Child")
# elif 13 <= age <= 17:
#     print("Teenager")
# elif 18 <= age <= 64:
#     print("Adult")
# elif age >= 65:
#     print("Senior")
# else:
#     print("Invalid age entered.")



# # Program to classify a number as positive, negative, or zero

# num = int(input("Enter an integer: "))

# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")



# # Program to check if a year is a leap year

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")



# # Simple calculator program

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter operator (+, -, *, /): ")

# if operator == '+':
#     print("Result:", num1 + num2)
# elif operator == '-':
#     print("Result:", num1 - num2)
# elif operator == '*':
#     print("Result:", num1 * num2)
# elif operator == '/':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Cannot divide by zero.")
# else:
#     print("Invalid operator.")



# # Using short-hand if-else to check if a number is even or odd

# x = 8
# result = "Even" if x % 2 == 0 else "Odd"
# print("The number is", result)



# # Program to calculate final price after discount

# # Input original price and discount percentage
# original_price = float(input("Enter the original price: "))
# discount_percent = float(input("Enter discount percentage: "))

# # Calculate discount amount and final price
# discount_amount = (discount_percent / 100) * original_price
# final_price = original_price - discount_amount

# # Output the final price
# print("Final price after discount:", final_price)



# # Program to calculate Body Mass Index (BMI)

# # Input weight in kilograms and height in meters
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))

# # Calculate BMI
# bmi = weight / (height ** 2)

# # Output BMI
# print("Your BMI is:", round(bmi, 2))
