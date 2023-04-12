def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def remain(a, b):
    return a % b


def division(a, b):
    try:                                            # блок try/except
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"



