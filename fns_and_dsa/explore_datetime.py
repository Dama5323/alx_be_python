from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()  # Gets the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Formats the date
    print("Current date and time:", formatted_date)

# Part 2: Calculate a future date based on user input
def calculate_future_date():
    days = int(input("Enter number of days to add: "))  # Get number of days from user
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # Add days to current date
    print("The date after", days, "days will be:", future_date.strftime("%Y-%m-%d"))

# Main function to call the two parts
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
