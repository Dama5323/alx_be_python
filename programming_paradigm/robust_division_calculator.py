# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Try performing the division
        result = num / den
        return f"Result: {result}"
    
    except ValueError:
        return "Error: Both inputs must be numeric."
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
