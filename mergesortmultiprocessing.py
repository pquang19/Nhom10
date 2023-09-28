import time
import threading
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

def mergesort_parallel(arr, left, right, depth=0):
    if left < right:
        if depth < MAX_DEPTH:
            middle = left + (right - left) // 2
            t1 = threading.Thread(target=mergesort_parallel, args=(arr, left, middle, depth+1))
            t2 = threading.Thread(target=mergesort_parallel, args=(arr, middle + 1, right, depth+1))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            merge(arr, left, right, middle)
        else:
            mergesort(arr, left, right)

MAX_DEPTH = 4  # Điều chỉnh độ sâu tối đa cho việc song song hóa
arr=create.arr

start_time = time . perf_counter ()
mergesort_parallel(arr, 0, len(arr) - 1)
end_time = time.perf_counter()

execution_time = end_time - start_time
print("Sorted Array:", arr)
print(f"Thời gian thực thi: {execution_time:.6f} giây")
