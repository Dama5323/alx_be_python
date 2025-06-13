import sys
from bank_account import BankAccount
from robust_division_calculator import safe_divide
from library_management import Book, Library

def handle_account_commands(args):
    account = BankAccount(100)  # Example starting balance
    command = args[0].lower()

    if command == "deposit":
        if len(args) != 2:
            print("Usage: deposit <amount>")
            return
        try:
            amount = float(args[1])
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
            account.display_balance()
        except ValueError:
            print("Error: Amount must be a number")

    elif command == "withdraw":
        if len(args) != 2:
            print("Usage: withdraw <amount>")
            return
        try:
            amount = float(args[1])
            if account.withdraw(amount):
                print(f"Withdrawn: ${amount:.2f}")
            else:
                print("Withdrawal failed: Insufficient funds")
            account.display_balance()
        except ValueError:
            print("Error: Amount must be a number")

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

def handle_library(args):
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    
    if not args:
        print("Available library commands: list, checkout, return")
        return
    
    command = args[0].lower()
    
    if command == "list":
        print("Available books:")
        library.list_available_books()
    elif command == "checkout":
        if len(args) != 2:
            print("Usage: library checkout <title>")
            return
        if library.check_out_book(args[1]):
            print(f"Successfully checked out: {args[1]}")
        else:
            print(f"Could not check out: {args[1]}")
    elif command == "return":
        if len(args) != 2:
            print("Usage: library return <title>")
            return
        if library.return_book(args[1]):
            print(f"Successfully returned: {args[1]}")
        else:
            print(f"Could not return: {args[1]}")
    else:
        print("Unknown library command. Use list, checkout, or return.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <mode> [args...]")
        print("Modes: account, divide, library")
        return

    mode = sys.argv[1].lower()
    args = sys.argv[2:]

    if mode == "account":
        handle_account_commands(args)
    elif mode == "divide":
        handle_division(args)
    elif mode == "library":
        handle_library(args)
    else:
        print("Unknown mode. Use 'account', 'divide', or 'library'.")

if __name__ == "__main__":
    main()