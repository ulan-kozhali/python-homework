num1 = int(input("Enter your first number for calculation: "))
num2 = int(input("Enter your second number for calculation: "))
val = input("Choose arithmetic value: +, -, *, /: ")

add = (num1+num2)
subt = (num1-num2)
mult = (num1*num2)
div = (num1/num2)

def total (num1, num2, val):
    if val == "+":
        print (f"{num1} + {num2} = {add}")
    elif val == "-":
        print (f"{num1} - {num2} = {subt}")
    elif val == "*":
        print (f"{num1} * {num2} = {mult}")
    elif val == "/":
        print (f"{num1} / {num2} = {subt}")
    else:
        print ("Choose right value: ")
total (num1, num2, val)

