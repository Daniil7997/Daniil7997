import time

"""
Задача:
Нахождение первой и последние позиций в отсортированном массиве

Сложность: Medium

Условие задачи: Дан целочисленный массив в порядке не убывания (это практически "в порядке возрастания", 
но данный термин предполагает что некоторые значения могут быть равны), необходимо найти первую и последнюю позиции целевого элемента, который надо отыскать.
Если целевого элемента нет в массиве, то надо вывести [-1; 1].
Алгоритм должен быть не медленнее, чем O(log n) по времени.

Пример:
Ввод: nums = [5,7,7,8,8,10], target = 8
Вывод: [3,4]

Объяснение:
Ввод: nums = [5,7,7,8,8,10], target = 6
Вывод: [-1,-1]

https://vk.com/python_django_programirovanie?w=wall-152111071_99018%2Fall
"""


def first_and_last(target, array):
    start = time.time()

    if target in array:
        result = []
        while target in array:
            index_target = array.index(target)
            result.append(index_target)
            array[index_target] = ' '
    else:
        return [-1, 1]

    print(f'Время потраченное на выполнение функции "first_and_last": {time.time() - start}')
    return result[0], result[-1]


def binary_search(target, array):

    if target not in array:
        return f'Значение {target} в массиве отсутствует'

    start = time.time()
    array = tuple(array)
    low = array.index(target)
    high = len(array) - 1
    result = []
    result.append(low)

    while len(result) != 2:
        mid = (low + high) // 2
        if array[mid] == target:
            low = mid
            if array[low] != array[low+1]:
                result.append(low)
        else:
            high = mid
    print(f'Время потраченное на выполнение функции: "binary_search" {time.time() - start}')
    return result


target = 4
array = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8]


for i in range(100000):
    array.append(4)

array.sort()

print(binary_search(target, array))
print(first_and_last(target, array))
