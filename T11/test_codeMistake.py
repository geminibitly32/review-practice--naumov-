def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

def check_password(password):
    if len(password) < 8:                  
        return "Слишком короткий!"          
    elif not any(char.isdigit() for char in password):
        return "Нет цифр!"                 
    else:
        return "Пароль надёжен!" 
print(check_password("qwerty"))

def calculate_sum(arr):
    total = 0
    for i in range(0, len(arr)):
        total += arr[i]
    return total
numbers = [10, 20, 30]
print(calculate_sum(numbers))
