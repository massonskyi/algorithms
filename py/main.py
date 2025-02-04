import random 
from sorting import shell_sort


def fill_array(size) -> list:
    array = []  # Создаем пустой массив
    for _ in range(size):
        array.append(random.randint(1, 100))
    return array

if __name__ == '__main__':
    arr = fill_array(1000)
    sorted_arr = shell_sort.shell_sort(arr)
    print("Отсортированный массив:", sorted_arr)