# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main interaction
def main():
    try:
        temp_input = input("Enter the temperature: ")
        temperature = float(temp_input)  # Validate that input is numeric
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result:.2f}°F")
    elif unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
