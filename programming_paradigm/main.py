# main.py

import sys
from bank_account import BankAccount
from robust_division_calculator import safe_divide

def handle_account_commands(args):
    account = BankAccount(100)  # Example starting balance
    command = args[0].lower()

    if command == "deposit":
        if len(args) != 2:
            print("Usage: deposit <amount>")
            return
        amount = float(args[1])
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
        account.display_balance()

    elif command == "withdraw":
        if len(args) != 2:
            print("Usage: withdraw <amount>")
            return
        amount = float(args[1])
        if account.withdraw(amount):
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Withdrawal failed: Insufficient funds")
        account.display_balance()

    elif command == "balance":
        account.display_balance()

    else:
        print("Unknown account command. Use deposit, withdraw, or balance.")

def handle_division(args):
    if len(args) != 2:
        print("Usage: divide <numerator> <denominator>")
        return
    numerator, denominator = args
    result = safe_divide(numerator, denominator)
    print(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <mode> [args...]")
        print("Modes: account, divide")
        return

    mode = sys.argv[1].lower()
    args = sys.argv[2:]

    if mode == "account":
        handle_account_commands(args)
    elif mode == "divide":
        handle_division(args)
    else:
        print("Unknown mode. Use 'account' or 'divide'.")

if __name__ == "__main__":
    main()
