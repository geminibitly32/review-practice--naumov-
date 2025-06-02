# calculator.py — простой калькулятор

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание второго числа из первого"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление с проверкой деления на ноль"""
    if b == 0:
        raise ValueError("Деление на ноль запрещено")
    return a / b

# Тесты
if __name__ == "__main__":
    print("Тестирование калькулятора:")
    print("Сложение: 5 + 3 =", add(5, 3))
    print("Вычитание: 5 - 3 =", subtract(5, 3))
    print("Умножение: 5 * 3 =", multiply(5, 3))
    print("Деление: 6 / 2 =", divide(6, 2))
