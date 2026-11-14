#try:
#    a = 10
#    b = 2
#    rezult = a / b
#except ZeroDivisionError:
#    print("Ошибка: Деление на 0 невозможно")
#else:
#    print(f"результат: {rezult}")
#finally:
#    print("Программа завершена")

class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Ошибка: Корень из отрицательного числа не определен")

try:
    num = int(input())
    rezult = square_root(num)
    print(rezult)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Ошибка: введено не число")