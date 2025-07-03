
# Python Exception Handling Examples

# 1. ValueError
try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# 2. FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# 3. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# 4. KeyError
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print(f"KeyError: {e}")

# 5. IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"IndexError: {e}")

# 6. AttributeError
try:
    x = 5
    x.append(10)
except AttributeError as e:
    print(f"AttributeError: {e}")

# 7. OverflowError
try:
    import math
    print(math.exp(1000))
except OverflowError as e:
    print(f"OverflowError: {e}")

# 8. Catch Any Exception
try:
    risky_code = 10 / 0
except Exception as e:
    print(f"Exception: {e}")
finally:
    print("Always runs.")
