import time
#Kết nối với file create tạo mảng dữ liệu đầu vào
import create

# Định nghĩa hàm mergesort để sắp xếp mảng arr từ vị trí left đến right (bao gồm)
def mergesort(arr, left, right):
    if left >= right:
        # Trường hợp cơ sở: nếu chỉ có một phần tử hoặc không có phần tử nào để sắp xếp, trả về mảng ban đầu
        return arr
    else:
        # Tìm giá trị trung bình của left và right
        middle = left + (right - left) // 2
        # Đệ quy sắp xếp mảng bên trái và bên phải của mảng con
        arr = mergesort(arr, left, middle)
        arr = mergesort(arr, middle + 1, right)
        # Hợp nhất hai mảng con đã sắp xếp thành một mảng đã sắp xếp
        arr = merge(arr, left, right, middle)
        return arr

# Định nghĩa hàm merge để hợp nhất hai mảng con thành một mảng đã sắp xếp
def merge(arr, left, right, middle):
    n1 = middle - left + 1
    n2 = right - middle

    left_array = [0] * n1
    right_array = [0] * n2

    # Sao chép dữ liệu từ mảng arr sang hai mảng con
    for i in range(n1):
        left_array[i] = arr[left + i]
    for j in range(n2):
        right_array[j] = arr[middle + 1 + j]

    i = 0
    j = 0
    k = left

    # So sánh và hợp nhất các phần tử từ hai mảng con vào mảng arr
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    # Sao chép các phần tử còn lại từ mảng con bên trái (nếu còn)
    while i < n1:
        arr[k] = left_array[i]
        i += 1
        k += 1

    # Sao chép các phần tử còn lại từ mảng con bên phải (nếu còn)
    while j < n2:
        arr[k] = right_array[j]
        j += 1
        k += 1

    return arr

# Lấy mảng cần sắp xếp từ module create (giả sử rằng module này chứa một biến tên là arr)
arr = create.arr

# Đo thời gian bắt đầu thực thi
start_time = time.perf_counter()

# Gọi hàm mergesort để sắp xếp mảng arr
array = mergesort(arr, 0, len(arr) - 1)

# In mảng đã sắp xếp
print("Sorted Array:", array)

# Đo thời gian kết thúc thực thi
end_time = time.perf_counter()

# Tính thời gian thực thi bằng cách trừ thời gian bắt đầu từ thời gian kết thúc
execution_time = end_time - start_time

# In thời gian thực thi
print(f"Thời gian thực thi: {execution_time:.6f} giây")
