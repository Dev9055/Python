try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    operation = input("Please enter the arithmetic operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ArithmeticError("Division by zero is not allowed.")
        else:
            result = num1 / num2
    else:
        raise ValueError("Invalid arithmetic operation.")

    print("The result of the arithmetic operation is:", result)

except ValueError as ve:
    print(ve)
    print("Please check your input and try again.")

except ArithmeticError as ae:
    print(ae)
    print("Please check your input and try again.")
