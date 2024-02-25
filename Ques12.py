salary=int(input("Salary:"))
age=int(input("Age:"))
if(salary >=20000 or age <=25):
    loan=int(input("Loan Amount: "))
    if(loan >50000):
        print("Maximum Loan Amount is 50000")
    else:
        print("Eligible for Loan")
    
else:
    print("Not eligible for loan")
