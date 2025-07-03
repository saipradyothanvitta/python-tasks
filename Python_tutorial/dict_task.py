# def display_menu():
#     print("\n--- Dictionary Operations Menu ---")
#     print("1. Add/Update Key-Value Pair")
#     print("2. Access Value by Key")
#     print("3. Remove Key-Value Pair")
#     print("4. Display All Keys")
#     print("5. Display All Values")
#     print("6. Exit")

# def main():
#     my_dict = {'name': 'python', 'age': 25}

#     while True:
#         display_menu()
#         choice = input("Enter your choice (1-6): ")

#         if choice == '1':
#             key = input("Enter key to add/update: ")
#             value = input("Enter value: ")
#             # Convert numeric input to int if possible
#             if value.isdigit():
#                 value = int(value)
#             my_dict[key] = value
#             print("Updated Dictionary:", my_dict)

#         elif choice == '2':
#             key = input("Enter the key to access: ")
#             if key in my_dict:
#                 print(f"Value for key '{key}':", my_dict[key])
#             else:
#                 print("Key not found in dictionary.")

#         elif choice == '3':
#             key = input("Enter the key to remove: ")
#             if key in my_dict:
#                 my_dict.pop(key)
#                 print("Updated Dictionary:", my_dict)
#             else:
#                 print("Key not found.")

#         elif choice == '4':
#             print("Keys in Dictionary:", list(my_dict.keys()))

#         elif choice == '5':
#             print("Values in Dictionary:", list(my_dict.values()))

#         elif choice == '6':
#             print("Exiting program. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please choose from 1 to 6.")

# if __name__ == "__main__":
#     main()
