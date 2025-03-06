import pytest
import random
from array import srt, search_sorted, merge_array, uniq_array, intersection_array

def generate_random_2d_array(rows, cols, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def test_srt():
    arr = generate_random_2d_array(3, 3)  # Генерация 3x3 массива
    sorted_arr = srt(arr)

    # Проверка, что каждая строка отсортирована
    for row in sorted_arr:
        assert row == sorted(row)

def test_search_sorted_found():
    sorted_arr = [[1, 2, 3], [4, 5, 6]]
    positions = search_sorted(sorted_arr, 5)
    assert positions == [(1, 1)]  # элемент 5 находится в позиции (1, 1)

def test_search_sorted_not_found():
    sorted_arr = [[1, 2, 3], [4, 5, 6]]
    positions = search_sorted(sorted_arr, 7)
    assert positions is None  # элемент 7 не найден

def test_merge_array():
    arr1 = generate_random_2d_array(2, 3)  # Генерация 2x3 массива
    arr2 = generate_random_2d_array(2, 3)  # Генерация 2x3 массива
    merged = merge_array(arr1, arr2)

    # Проверка, что результат имеет правильный размер
    assert len(merged) == 2  # Должно быть 2 строки
    assert len(merged[0]) == 6  # Каждая строка должна содержать 6 элементов
    assert len(merged[1]) == 6  # Каждая строка должна содержать 6 элементов

def test_uniq_array():
    arr = [[1, 2, 3], [1, 2, 3], [4, 5, 6]]
    unique = uniq_array(arr)
    assert unique == [[1, 2, 3], [4, 5, 6]]  # Проверка на уникальные строки

def test_intersection_array():
    arr1 = [[1, 2, 3], [4, 5, 6]]
    arr2 = [[4, 5, 6], [7, 8, 9]]
    intersection = intersection_array(arr1, arr2)
    assert intersection == [[4, 5, 6]]  # Проверка на пересечения

# Запуск тестов
if __name__ == "__main__":
    pytest.main()