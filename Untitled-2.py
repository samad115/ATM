class ATM:
    def _init_(self, total_amount, username, pin):
        self.total_amount = total_amount
        self.username = username
        self.pin = pin
        self.transactions = []
    def authenticate_user(self, username, pin):
        return username == self.username and pin == self.pin
    def check_balance(self):
        return self.total_amount
    def withdraw_cash(self, amount):
        if amount > 0 and self.total_amount >= amount:
            self.total_amount -= amount
            self.transactions.append(-amount)
            return True
        else:
            return False
    def deposit_cash(self, amount):
        if amount > 0:
            self.total_amount +=amount 
            self.transactions.append(amount)
            return True
        else:
            return False
    def mini_statement(self):
        if len(self.transactions) == 0:
            return "No transactions yet."
        else:
            statement = "Mini Statement:\n"
            for i in range(-1, -4, -1):
                if abs(i) <= len(self.transactions):
                    transaction = self.transactions[i]
                    statement += f"{abs(transaction)} {'Deposited' if transaction > 0 else 'Withdrawn'}\n"
            return statement
def main():
    atm = ATM(5000, "user123", "1234")
    username = input("Enter username: ")
    pin = input("Enter PIN: ")
    if atm.authenticate_user(username, pin):
        print("Authentication successful!")
    else:
        print("Authentication failed. Exiting...")
        return
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Mini Statement")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            balance = atm.check_balance()
            print(f"Your balance is ${balance}")
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            if atm.withdraw_cash(amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed. Insufficient balance or invalid amount.")
        elif choice == '3':
            amount = float(input("Enter deposit amount: "))
            if atm.deposit_cash(amount):
                print("Deposit successful.")
            else:
                print("Deposit failed. Invalid amount.")
        elif choice == '4':
            statement = atm.mini_statement()
            print(statement)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "_main_":
    main()
