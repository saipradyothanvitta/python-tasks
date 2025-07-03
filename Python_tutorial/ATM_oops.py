class ATM:
    def __init__(self, initial_balance=0):
        """
        Initializes the ATM with an optional initial balance.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__balance = initial_balance  # Encapsulating the balance

    def display_menu(self):
        """
        Displays the ATM menu options.
        """
        print("\nATM Menu:")
        print("1. Credit")
        print("2. Debit")
        print("3. Check Balance")
        print("4. Exit")

    def credit(self):
        """
        Handles the credit operation, adding funds to the account.
        """
        try:
            amount = float(input("Enter amount to credit: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                self.__balance += amount
                print(f"Rs{amount:.2f} credited to your account.")
        except ValueError:
            print("Invalid input. Please enter a numerical amount.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def debit(self):
        """
        Handles the debit operation, withdrawing funds from the account.
        """
        try:
            amount = float(input("Enter amount to debit: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            elif amount > self.__balance:
                print("Insufficient balance.")
            else:
                self.__balance -= amount
                print(f"Rs{amount:.2f} debited from your account.")
        except ValueError:
            print("Invalid input. Please enter a numerical amount.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def check_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Your current balance is: Rs{self.__balance:.2f}")

    def run(self):
        """
        Runs the main ATM loop, interacting with the user.
        """
        print("Welcome to the OOP ATM!")
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.credit()
            elif choice == '2':
                self.debit()
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of the ATM and run it
if __name__ == "__main__":
    my_atm = ATM(initial_balance=1000) # You can set an initial balance here
    my_atm.run()