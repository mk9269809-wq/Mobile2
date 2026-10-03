# Germany Salary Calculator - Pro Version
print("--- Germany Salary Calculator ---")
salary = int(input("Monthly Gross Salary (Euro) ? "))
social = salary * 0.20
if salary < 1000:
    income_tax = 0
elif salary < 3000:
    income_tax = salary * 0.15
elif salary < 5000:
    income_tax = salary * 0.25
else:
    income_tax = salary * 0.32
total_tax = social + income_tax
net_salary = salary - total_tax
print("\n------ Result ------")
print(f"Gross Salary: {salary} Euro")
print(f"Social Security (20%): {int(social)} Euro")
print(f"Income Tax: {int(income_tax)} Euro")
print(f"Total Tax: {int(total_tax)} Euro")
print(f"Net Bachega: {int(net_salary)} Euro")
