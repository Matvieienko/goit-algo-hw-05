def binary_search_with_iterations(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    iterations = 0  # Лічильник ітерацій
    upper_bound = None  # Верхня межа

    while left <= right:
        iterations += 1
        mid = (left + right) // 2  # Середній елемент

        if sorted_array[mid] == target:
            # Якщо знайдено точний збіг, оновлюємо верхню межу
            upper_bound = sorted_array[mid]
            return (iterations, upper_bound)
        elif sorted_array[mid] < target:
            # Переміщуємо ліву межу, якщо середнє значення менше за ціль
            left = mid + 1
        else:
            # Оновлюємо верхню межу та переміщуємо праву межу
            upper_bound = sorted_array[mid]
            right = mid - 1

    # Повертаємо кількість ітерацій і найменший елемент, який є більшим або рівним заданому значенню
    return (iterations, upper_bound)

# Тестуємо функцію
sorted_array = [0.1, 0.5, 1.3, 2.7, 3.9, 5.1, 7.6]
target = 2.0
result = binary_search_with_iterations(sorted_array, target)
print(f"Для числа {target}: Кількість ітерацій = {result[0]}, Верхня межа = {result[1]}")

target = 4.0
result = binary_search_with_iterations(sorted_array, target)
print(f"Для числа {target}: Кількість ітерацій = {result[0]}, Верхня межа = {result[1]}")

target = 7.6
result = binary_search_with_iterations(sorted_array, target)
print(f"Для числа {target}: Кількість ітерацій = {result[0]}, Верхня межа = {result[1]}")