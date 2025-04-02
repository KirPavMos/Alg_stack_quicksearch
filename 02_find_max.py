# 02 Напишите рекурсивную функцию для нахождения максимального
# элемента в списке, используя подход "Разделяй и властвуй"

def find_max(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])

    return max(left_max, right_max)

numbers = [3, 7, 2, 9, 5, 1, 8]
print(find_max(numbers))