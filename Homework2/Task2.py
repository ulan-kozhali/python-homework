num1 = int(input("Enter your first number for calculation: "))
num2 = int(input("Enter your second number for calculation: "))

add = (num1+num2)
subt = (num1-num2)
mult = (num1*num2)
div = (num1/num2)


addition = input("If you want to make addition of your number, please press 1: ")
def show_add (add, subt, mult, div):
    if int(addition) == 1:
        print (f"Your addition number is: {add}")
    else:
        print ()
show_add (add, subt, mult, div)


subtraction = input("If you want to make subtraction of your number, please press 2: ")
def show_subt (add, subt, mult, div):
    if int(subtraction) == 2:
        print (f"Your subtraction number is: {subt}")
    else:
        print ()
show_subt (add, subt, mult, div)

multiplication = input("If you want to make multiplication of your number, please press 3: ")
def show_mult (add, subt, mult, div):
    if int(multiplication) == 3:
        print (f"Your multiplication number is: {mult}")
    else:
        print ()
show_mult (add, subt, mult, div)

division = input("If you want to make division of your number, please press 4: ")
def show_div (add, subt, mult, div):
    if int(division) == 4:
        print (f"Your division number is: {div}")
    else:
        print ()
show_div (add, subt, mult, div)
