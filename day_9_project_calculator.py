def ask_first():
    """Asks about the first number."""
    first_num = int(input("What is your first number? "))
    return first_num

def ask_operator():
    """Asks about the operator you want to calculate with."""
    operator = input("Please choose an operator (+,-,*,/,**) ")
    return operator

def ask_second():
    """Asks about the second number."""
    second_num = int(input("What is the second number? "))
    return second_num

def ask_continue():
    """Asks if the user wants to continue computing with the previous result, start a new result or exit the program."""
    question = input("Type 'y' if you want to continue calculating with your result. Type 'n' if you want to start a new calculation. Type 'exit' if you want to exit the program. ")
    return question

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def power(n1,n2):
    return n1**n2

#To Do: Somehow pack the if, elif statements in a function
def program():
    """Asks numbers and the operator and gives the user a choice whether the user wants to continue calculating
    with the result of a computation, start a new conputation or exit the program."""
    try:
        first_num = ask_first()
        second_num = ask_second()
        op = ask_operator()
        if op == '+':
            result = add(first_num,second_num)
        elif op == '-':
            result = sub(first_num,second_num)
        elif op == '*':
            result = mult(first_num,second_num)
        elif op == '/':
            result = div(first_num,second_num)
        elif op == '**':
            result = power(first_num,second_num)
        print(str(first_num) + " " + op + " " + str(second_num) + " = " + str(result))
    except ValueError:
        print("Something was wrong with your input.")
        program()

    cont = True
    while cont==True:
        ans = ask_continue()
        if ans == 'n':
            program()
        elif ans == 'exit':
            return None
        elif ans == 'y':
            second_num = ask_second()
            op = ask_operator()
            x = result
            if op == '+':
                result = add(result, second_num)
            elif op == '-':
                result = sub(result, second_num)
            elif op == '*':
                result = mult(result, second_num)
            elif op == '/':
                result = div(result, second_num)
            elif op == '**':
                result = power(result, second_num)
            print(str(x) + " " + op + " " + str(second_num) + " = " + str(result))
        else:
            print("Invalid input.")
            continue

program()
