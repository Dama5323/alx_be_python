# Daily Task Reminder System

print("Daily Priority Task Reminder")
print("---------------------------")

# Get task details from user
task = input("Enter your priority task for today: ")
priority = input("Enter task priority (high/medium/low): ").lower()
time_bound = input("Is this task time-sensitive? (yes/no): ").lower()

# Process and generate reminder
time_sensitive_part = " that requires immediate attention today!" if time_bound == "yes" else "."

match priority:
    case "high":
        reminder = f"🚨 HIGH PRIORITY: {task}{time_sensitive_part}"
    case "medium":
        reminder = f"⚠️ Medium priority: {task}{time_sensitive_part}"
    case "low":
        reminder = f"✅ Low priority: {task}{time_sensitive_part}"
    case _:
        reminder = f"Task: {task}{time_sensitive_part}"

# Display the reminder
print("\n📌 Today's Task Reminder:")
print(reminder)

# Additional urgency for time-sensitive high priority tasks
if priority == "high" and time_bound == "yes":
    print("\n⏰ Warning! This is both high priority and time-sensitive!")
    print("Consider working on this first thing today!")