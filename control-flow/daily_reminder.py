# Daily Task Reminder System

# Get task details from user with exact required prompts
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process and generate reminder
time_sensitive_part = " that requires immediate attention today!" if time_bound == "yes" else "."

match priority:
    case "high":
        reminder = f"HIGH PRIORITY: {task}{time_sensitive_part}"
    case "medium":
        reminder = f"Medium priority: {task}{time_sensitive_part}"
    case "low":
        reminder = f"Low priority: {task}{time_sensitive_part}"
    case _:
        reminder = f"Task: {task}{time_sensitive_part}"

# Display the reminder
print(reminder)

# Additional check for time-bound tasks
if time_bound == "yes":
    print("Immediate action required!")