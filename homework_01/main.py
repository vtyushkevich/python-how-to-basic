"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    return list(num * num for num in numbers)

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


print(power_numbers(1, 2, 5, 7))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(numbers):
    results = []
    for num1 in numbers:
        if type(num1) is int and num1 != 0:
            k = True
            for i in range(2, int(num1 // 2 + 1)):
                if (num1 % i) == 0:
                    k = False
                    break
            if k and num1 != 1:
                results.append(num1)
    return results


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == "even":
        return list(filter(lambda x: x % 2 == 0, numbers))
    if filter_type == "odd":
        return list(filter(lambda x: x % 2 != 0, numbers))
    if filter_type == "prime":
        return is_prime(numbers)


for num_type in [ODD, EVEN, PRIME]:
    print(filter_numbers(list(range(0, 20)), num_type))

