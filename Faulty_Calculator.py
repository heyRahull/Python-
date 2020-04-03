# FAULTY CALCULATOR
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# The program takes an operator and two numbers from the user
# and outputs the result

print("\nWelcome to the Faulty Calc : This is developed by Rahul Agarwal\n")


def calculator():
    operation = input('''
        Please type in the operation that you want to perform :
        + : for ADDITION
        - : for SUBTRACTION
        * : for MULTIPLICATION
        / : for DIVISION
        ** : for POWER
        % : for MODULO\n
        Enter Your choice :''')

    print("\nThe Operation that is being performed is : ", operation, "\n")
    num1 = int(input("Enter Number 1 :"))
    num2 = int(input("Enter Number 2 :"))

    if operation == '+':
        if num1 == 56 and num2 == 9:
            print("The Result of ", num1, operation, num2, "is :", 77, "       ----------THIS IS A FAULTY OUTPUT------------")
        else:
            print("The Result of ", num1, operation, num2, "is :", num1 + num2)

    elif operation == '-':
        print("The Result of ", num1, operation, num2, "is :", num1 - num2)

    elif operation == '*':
        if num1 == 45 and num2 == 3:
            print("The Result of ", num1, operation, num2, "is :", 555, "       -----------THIS IS A FAULTY OUTPUT------------")
        else:
            print("The Result of ", num1, operation, num2, "is :", num1 * num2)

    elif operation == '/':
        if num1 == 56 and num2 == 6:
            print("The Result of ", num1, operation, num2, "is :", 4, "        -------------THIS IS A FAULTY OUTPUT------------")
        else:
            print("The Result of ", num1, operation, num2, "is :", num1 / num2)

    elif operation == '**':
        print("The Result of ", num1, operation, num2, "is :", num1 ** num2)

    elif operation == '%':
        print("The Result of ", num1, operation, num2, "is :", num1 % num2)


def again():
    run_again = input(''' \nDo you want to calculate again?
        Please type y for YES or n for NO : ''')

    if run_again == 'y' or run_again == 'Y' :
        calculator()
        again()
    elif run_again == 'n' or run_again == 'N':
        print("SEE YOU LATER")
    else:
        again()


calculator()
again()
