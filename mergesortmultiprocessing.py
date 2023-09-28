import time
import threading
#Kết nối với file create để tạo mảng dữ liệu
import create

# Hàm sắp xếp mảng bằng thuật toán sắp xếp trộn
def mergesort(arr, left, right):
    if left >= right:
        return arr
    else:
        middle = left + (right - left) // 2
        # Đệ quy: Sắp xếp mảng bên trái và bên phải của mảng con
        arr = mergesort(arr, left, middle)
        arr = mergesort(arr, middle + 1, right)
        # Hợp nhất hai mảng con đã sắp xếp thành một mảng đã sắp xếp
        arr = merge(arr, left, right, middle)
        return arr

# Hàm hợp nhất hai mảng con thành một mảng đã sắp xếp
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

# Hàm sắp xếp mảng song song bằng cách sử dụng luồng (threading)
def mergesort_parallel(arr, left, right, depth=0):
    if left < right:
        if depth < MAX_DEPTH:
            middle = left + (right - left) // 2
            # Tạo và bắt đầu hai luồng để sắp xếp mảng bên trái và bên phải của mảng con
            t1 = threading.Thread(target=mergesort_parallel, args=(arr, left, middle, depth + 1))
            t2 = threading.Thread(target=mergesort_parallel, args=(arr, middle + 1, right, depth + 1))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            # Hợp nhất hai mảng con đã sắp xếp
            merge(arr, left, right, middle)
        else:
            # Đạt đến độ sâu tối đa, sử dụng sắp xếp trộn thông thường
            mergesort(arr, left, right)

MAX_DEPTH = 4  # Điều chỉnh độ sâu tối đa cho việc song song hóa
arr = create.arr

# Đo thời gian bắt đầu thực thi
start_time = time.perf_counter()

# Gọi hàm sắp xếp mảng song song
mergesort_parallel(arr, 0, len(arr) - 1)

# Đo thời gian kết thúc thực thi
end_time = time.perf_counter()

# In mảng đã sắp xếp và thời gian thực thi
print("Sorted Array:", arr)
print(f"Thời gian thực thi: {end_time - start_time:.6f} giây")
