import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время до выполнения
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Засекаем время после выполнения
        print(f"Время выполнения функции {func.__name__}: {(end_time - start_time) * 1000} мс")
        return result
    return wrapper


@time_decorator
def shell_sort(arr):
    n = len(arr)
    gap = 1
    
    while gap < n // 3:
        gap = 3 * gap + 1
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 3
    
    return arr