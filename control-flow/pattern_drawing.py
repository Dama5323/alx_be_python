# Pattern Drawing with Nested Loops

# Get user input for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    for _ in range(size):
        print("*", end="")  # Print without space to match exact requirements
    
    # Move to next line after completing a row
    print()
    
    # Increment row counter
    row += 1