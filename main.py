from calculator_modules.operation.basic import *
from calculator_modules.operation.advanced import *
from calculator_modules.operation.trigonometry import *

def main():
    print("Добро пожаловать в жопу калькулятора")
    a = float(input("Введи размер первого яйца: "))
    b = float(input("Введи число 2: "))
    operation = input("Введите операцию (+, -, *, /, **, sqrt, sin, cos, tg, ctg): ")
    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtrack(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    elif operation == "**":
        result = power(a, b)
    elif operation == "sqrt":
        result = square_root(a, b)
    elif operation == "sin":
        result = sin(a)
    elif operation == "cos":
        result = cos(a)
    elif operation == "tg":
        result = tg(a)
    elif operation == "ctg":
        result = ctg(a)
    else:
        result = "Оператора нету"

    print(f"Результат: {result}")

if __name__ == "__main__":
    main()