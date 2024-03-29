operator=input("enter the operator + - * / : ")
num1=float(input("enter a number :"))
num2=float(input("enter a number:"))

if operator== "+":
    result=num1+num2
    print(round(result,3))
elif operator== "-":
    result=num1-num2
    print(round(result,3))
elif operator== "*":
    result=num1*num2
    print(round(result,2))
elif operator=="/":
    result=num1/num2
    print(round(result,2))
else:
    print(f"{operator} it is not defined")