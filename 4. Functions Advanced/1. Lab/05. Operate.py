def operate(sign, *args):

    if not args:
        return None  # return None or raise an error if no arguments are provided

    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for i in args[1:]:
            result -= i
        return result

    def multiply():
        result = 1
        for i in args:
            result *= i
        return result

    def divide():
        result = args[0]
        for i in args[1:]:
            result /= i
        return result

    if sign == "+":
        return add()
    elif sign == "-":  # corrected from "=" to "-"
        return subtract()
    elif sign == "*":
        return multiply()
    elif sign == "/":
        return divide()
