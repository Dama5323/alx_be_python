
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
                               
monthly_savings = monthly_income - monthly_expenses


annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
Projected_Savings =monthly_savings * 12+ (monthly_savings * 12 * 0.05)


print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings:.2f}.")
