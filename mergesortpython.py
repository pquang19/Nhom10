import time

start_time = time.perf_counter()

def mergesort(arr, left, right):
    if left >= right:
        return arr
    else:
        middle = left+(right-left)//2
        arr = mergesort(arr, left, middle)
        arr = mergesort(arr, middle+1, right)
        arr = merge(arr, left, right, middle)
        return arr


def merge(arr, left, right, middle):
    n1 = middle - left + 1
    n2 = right - middle

    left_array = [0] * n1
    right_array = [0] * n2

    for i in range(n1):
        left_array[i] = arr[left + i]
    for j in range(n2):
        right_array[j] = arr[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_array[j]
        j += 1
        k += 1

    return arr


arr = [38, 27, 43, 3, 9, 82, 10]
array = mergesort(arr, 0, len(arr) - 1)
print("Sorted Array:", array)

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Thời gian thực thi: {execution_time:.6f} giây")


