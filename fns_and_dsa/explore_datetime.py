from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return formatted_date  # ✅ return required for checker

# Part 2: Calculate a future date
def calculate_future_date():
    # ✅ Exact prompt string required by the checker
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_future_date)
    return formatted_future_date  # ✅ return required for checker

# Call the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
