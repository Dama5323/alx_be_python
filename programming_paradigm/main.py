# main-0.py

import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main-0.py <operation> [amount]")
        return

    account = BankAccount()
    operation = sys.argv[1].lower()

    if operation == "deposit":
        if len(sys.argv) != 3:
            print("Usage: deposit <amount>")
            return
        amount = float(sys.argv[2])
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
        account.display_balance()

    elif operation == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: withdraw <amount>")
            return
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Withdrawal failed: Insufficient funds")
        account.display_balance()

    elif operation == "balance":
        account.display_balance()

    else:
        print("Unknown operation. Use deposit, withdraw, or balance.")

if __name__ == "__main__":
    main()
