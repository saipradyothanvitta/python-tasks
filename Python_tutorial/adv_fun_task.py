# def square_all(numbers):
#     return list(map(lambda x: x**2, numbers))

# # Example usage:
# print(square_all([1, 2, 3, 4]))  # Output: [1, 4, 9, 16]



# def filter_positive(numbers):
#     return list(filter(lambda x: x > 0, numbers))

# # Example usage:
# print(filter_positive([-3, 0, 4, -1, 7]))  # Output: [4, 7]



# from functools import reduce

# def calculate_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return reduce(lambda x, y: x * y, range(1, n + 1))

# # Example usage:
# print(calculate_factorial(5))  # Output: 120



# from functools import reduce

# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     return reduce(lambda count, char: count + (1 if char in vowels else 0), string, 0)

# # Example usage:
# print(count_vowels("Python is awesome"))  # Output: 6
