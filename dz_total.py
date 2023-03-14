# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования


import cmath
import logging

# Настройка логгера
logging.basicConfig(filename='calculator.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Функции для выполнения арифметических операций
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# Функция для выбора операции
def select_operation():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    choice = input("Введите номер операции (1/2/3/4/5): ")
    return choice

# Функция для ввода чисел
def enter_numbers():
    x = complex(input("Введите первое число: "))
    y = complex(input("Введите второе число: "))
    return x, y

# Главная функция
def main():
    # Ввод чисел и выбор операции
    x, y = enter_numbers()
    choice = select_operation()

    # Выполнение операции и вывод результата
    if choice == '1':
        result = add(x, y)
    elif choice == '2':
        result = subtract(x, y)
    elif choice == '3':
        result = multiply(x, y)
    elif choice == '4':
        result = divide(x, y)
    elif choice == '5':
        result = power(x, y)
    else:
        print("Некорректный ввод.")
        return

    print("Результат:", result)

    # Запись операции в лог
    logging.info(f"Операция: {choice}; Числа: {x}, {y}; Результат: {result}")

if __name__ == '__main__':
    main()



