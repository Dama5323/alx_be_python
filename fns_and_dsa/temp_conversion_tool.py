# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main user interaction
def main():
    try:
        temp_input = input("Enter the temperature: ")
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ")

        try:
            temperature = float(temp_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        unit = unit.strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is {converted:.2f} Fahrenheit")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is {converted:.2f} Celsius")
        else:
            print("Invalid unit. Please enter C or F.")

    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
