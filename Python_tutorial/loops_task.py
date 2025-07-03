# # Sum of squares from 1 to 5
# sum_squares = 0
# for i in range(1, 6):
#     sum_squares += i ** 2
# print("Sum of squares from 1 to 5:", sum_squares)


# # Countdown from 5 to 1
# count = 5
# while count >= 1:
#     print(count)
#     count -= 1


# # Multiplication table for a user-specified number
# num = int(input("Enter a number for the multiplication table: "))

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")
#     print("-" * 20)  # separator between tables


# # Sum of even numbers between 0 and 10
# sum_even = 0
# for i in range(0, 11, 2):
#     sum_even += i
# print("Sum of even numbers from 0 to 10:", sum_even)



# # Sum from 1 to a given number
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print(f"Sum from 1 to {n} is:", total)



# # Display numbers from a list
# numbers = [5, 10, 15, 20, 25]
# for num in numbers:
#     print(num)



# # Display numbers from -10 to -1
# for i in range(-10, 0):
#     print(i)



# # Display all prime numbers within a range
# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))

# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
