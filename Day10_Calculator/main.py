import operator
from day10_calculator_art import logo

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

def operation(n1, op, n2):
    return ops[op](n1, n2)

calc_stop = False

while (not calc_stop):
    print(logo)
    f_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    
    keep_calc_stop = False
    
    while (not keep_calc_stop):
        operator = input("Pick an operation: ")
        if (operator not in ops):
            keep_calc_stop = True
            calc_stop = True
            print("You didn't input the corret operator. We cannot calculate. Bye.")
            
        else:
            l_number = float(input("What's the next number?: "))
            result = operation(f_number, operator, l_number)

            print(f"{f_number} {operator} {l_number} = {result}")
            question = input(f"Type 'y' to continue calculating with {result}, Type 'n' to start a new calculation, or Type 'quit' to stop: ")
        
            if (question == "y"):
                f_number = result
            elif (question == "n"):
                keep_calc_stop = True
            else:
                keep_calc_stop = True
                calc_stop = True
                print("Thank you for using our calculator!")        
