# Daily Task Reminder System

# Get task details from user with exact required prompts
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task with match-case
match priority:
    case "high":
        priority_msg = "HIGH PRIORITY"
    case "medium":
        priority_msg = "Medium priority"
    case "low":
        priority_msg = "Low priority"
    case _:
        priority_msg = "Task"

# Add time sensitivity notice
time_notice = " that requires immediate attention today!" if time_bound == "yes" else "."

# Print the formatted reminder
print(f"Reminder: {priority_msg}: {task}{time_notice}")

# Additional time-bound notice
if time_bound == "yes":
    print("Immediate action required!")
    