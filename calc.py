#Title
print("Calculator")

#Enter numbers for calculation
num1 = float(input("Enter First Number: "))
oper = input("Enter Operation: ")
num2 = float(input("Enter Second Number: "))

#Determining operations
if oper == "+": 
    print(num1 , " + " , num2 , " = " , num1+num2)
elif oper == "-": 
    print(num1 , " - " , num2 , " = " , num1-num2)
elif oper == "/": 
    print(num1 , " / " , num2 , " = " , num1/num2)
elif oper == "*": 
    print(num1 , " * " , num2 , " = " , num1*num2)
elif oper == "=":
    print("Error")