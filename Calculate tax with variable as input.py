income = float(input("Enter the annual income: "))

if(income <= 85528):
    tax = 0.18*income-556.02
else:
    tax = (income-85528)*0.32 + 14839.02

if tax >= 0:
    tax = round(tax,0)
else:
    tax=0.0
print("The tax is:", tax, "thalers")
