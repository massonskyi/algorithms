package pkg

import (
	"fmt"
	"time"
)

// timeDecorator оборачивает функцию и замеряет её время выполнения
func timeDecorator(f func([]int) []int) func([]int) []int {
	return func(arr []int) []int {
		start := time.Now()           // Засекаем время начала
		result := f(arr)              // Выполняем функцию
		duration := time.Since(start) // Засекаем время окончания
		fmt.Printf("Время выполнения функции: %v мс\n", duration.Milliseconds())
		return result
	}
}

// shellSort сортировка Шелла
func shellSort(arr []int) []int {
	n := len(arr)
	gap := 1

	// Вычисляем начальный промежуток по формуле Кнута
	for gap < n/3 {
		gap = 3*gap + 1
	}

	// Последовательно уменьшаем промежуток
	for gap > 0 {
		// Применяем сортировку вставками для текущего промежутка
		for i := gap; i < n; i++ {
			temp := arr[i]
			j := i
			// Сдвигаем элементы, пока не найдем позицию для вставки
			for j >= gap && arr[j-gap] > temp {
				arr[j] = arr[j-gap]
				j -= gap
			}
			arr[j] = temp
		}
		// Уменьшаем промежуток
		gap = gap / 3
	}

	return arr
}
