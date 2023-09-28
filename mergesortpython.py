import time
import create 

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


arr=create.arr
#arr = [5, 8, 4, 14, 23, 80, 6, 72, 57, 73, 53, 47, 27, 82, 65, 69, 57, 94, 48, 59, 36, 93, 32, 54, 40, 78, 95, 67, 11, 66, 51, 70, 62, 79, 29, 29, 36, 93, 48, 37, 82, 55, 98, 31, 33, 2, 36, 21, 47, 60, 38, 96, 70, 65, 64, 0, 10, 23, 78, 36, 31, 4, 82, 92, 2, 20, 2, 74, 17, 15, 65, 89, 97, 60, 56, 4, 41, 15, 56, 60, 39, 55, 47, 79, 34, 29, 96, 31, 8, 80, 82, 14, 85, 26, 88, 1, 5, 51, 33, 24]
start_time = time.perf_counter()
array = mergesort(arr, 0, len(arr) - 1)
print("Sorted Array:", array)

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Thời gian thực thi: {execution_time:.6f} giây")


