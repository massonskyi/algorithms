# [1,2,3]
# [1,4,9]
import time
import numpy as np

array = np.random.rand(1000000)


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f'function {func.__name__} worked during {(end_time - start_time):.10f} second')
        return result
    return wrapper

# n * log(n)


@timer
def power(array: list[int], exp: int = 2) -> list[int]:
    return sorted(list(map(lambda x: x**exp, array)))

# O(n)


@timer
def foo(nums: list[int]) -> list[int]:
    """
    Функция, которая получает на вход сортированный массив целых чисел и возвращает квадраты этих чисел.
    """
    n = len(nums)  # вычисляем длину массива
    result = [0] * n  # создаем пустой массив той же длины
    left, right = 0, n - 1  # задаем начальные значения указателей на крайние элементы массива
    for i in range(n - 1, -1, -1):  # итерируемся по массиву в обратном порядке
        # выбираем большее число по модулю и записываем его квадрат
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1  # перемещаем указатель слева на следующий элемент
        else:
            result[i] = nums[right] ** 2
            right -= 1  # перемещаем указатель справа на предыдущий элемент
    return result


def test():
    assert power([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert power([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == \
        [0, 1, 4, 4, 9, 9, 16, 16, 25, 25]
    assert foo([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == \
        [0, 1, 4, 4, 9, 9, 16, 16, 25, 25]
    assert foo([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
