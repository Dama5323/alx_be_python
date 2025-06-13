def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling for:
    - Division by zero
    - Non-numeric inputs
    
    Args:
        numerator: The numerator (string or numeric)
        denominator: The denominator (string or numeric)
        
    Returns:
        str: Either the result message or error message
    """
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."