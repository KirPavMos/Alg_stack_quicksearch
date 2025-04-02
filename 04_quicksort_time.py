# Проанализируйте время выполнения быстрой сортировки на
# списках различной длины (например, 10, 100, 1000 элементов)
# и сравните её с другими сортировками, такими как сортировка
# вставками

import time
import random

def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def test_sort(sort_func, arr):
    arr_copy = arr.copy()
    start = time.time()
    sort_func(arr_copy)
    end = time.time()
    return end - start

sizes = [10, 100, 1000]
results = {}

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    results[size] = {
        "quicksort": test_sort(quicksort, arr),
        "insertion_sort": test_sort(insertion_sort, arr),
        "timsort (sorted)": test_sort(sorted, arr)
    }
for size, times in results.items():
    print(f"\nРазмер массива: {size}")
    for algo, t in times.items():
        print(f"{algo:20}: {t:.6f} сек")