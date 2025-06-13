# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den

        return f"Result is: {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Inputs must be numeric."
