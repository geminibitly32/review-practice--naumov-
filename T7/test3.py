def calculate_positive_average(numbers):
    """
    Вычисляет среднее арифметическое положительных элементов в списке `numbers`.
    Возвращает 0, если положительных элементов нет.
    """
    total = 0   # Сумма положительных чисел
    count = 0   # Количество положительных чисел

    for num in numbers:
        if num > 0:
            total += num
            count += 1

    if count > 0:
        average = total / count  # Строка A: деление только при наличии положительных
    else:
        average = 0  # Если положительных нет

    return average
