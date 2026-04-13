salary = float(input("Enter your salary in LPA: "))
tax = 0
if salary <= 2.5:
    tax = 0
    print("No tax for salary up to 2.5 LPA")

elif salary <= 5:
    tax = (salary - 2.5) * 0.05
elif salary <= 10:
    tax = 0.125 + (salary - 5) * 0.10
else:
    tax = 0.125 + 0.50 + (salary - 10) * 0.15
print("Your total tax is:", tax, "Lakhs")
