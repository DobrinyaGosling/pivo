
def input_arr():
    arr = []
    rows = int(input("Enter rows: "))

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        arr.append(row)
    print(arr)
    return arr


def srt(arr: list):

    for row in arr:
        n = len(row)
        for i in range(n):
            for j in range(0, n - i - 1):
                if row[j] > row[j+1]:
                    row[j], row[j+1] = row[j+1], row[j]
    return arr


def search_sorted(sorted_arr, el: int):
    positions_of_el = []

    for i, row in enumerate(sorted_arr):
        for j in range(len(row)):
            if row[j] == el:
                tuple_position = (i, j)
                positions_of_el.append(tuple_position)

    if len(positions_of_el) > 0:
        return positions_of_el
    else:
        return None


def merge_array(arr1: list, arr2: list):
    # Предполагаем, что arr1 и arr2 одинаковой длины
    length = len(arr1)
    merged_array = [0] * length  # Создаем массив фиксированного размера

    for i in range(length):
        merged_array[i] = arr1[i] + arr2[i]  # Суммируем соответствующие элементы

    # Сортируем результирующий массив
    merged_array.sort()
    return merged_array


def uniq_array(arr: list):
    uniq_arr = []

    for row in arr:
        if row not in uniq_arr:
            uniq_arr.append(row)
    return uniq_arr


def intersection_array(arr1: list, arr2: list):
    intersection_arr = []
    uniq_arr1 = uniq_array(arr1)
    uniq_arr2 = uniq_array(arr2)

    for row1 in uniq_arr1:
        for row2 in uniq_arr2:
            if row1 == row2:
                intersection_arr.append(row1)
    print(intersection_arr)
    return intersection_arr


#intersection_arr([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, 2, 3], [1, 2, 3], [0, 5, 6], [7, 8, 9], [1, 2, 3]])
