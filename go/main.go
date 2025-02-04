package main

import (
	. "algorithms/cmd/pkg/shell_sort"
	"fmt"
)

func main() {
	// Оборачиваем функцию shellSort в декоратор
	decoratedSort := timeDecorator(shellSort)

	// Пример использования
	arr := []int{5, 2, 9, 1, 5, 6}
	sortedArr := decoratedSort(arr)
	fmt.Println("Отсортированный массив:", sortedArr)
}
