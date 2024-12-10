#Nama : Dwi Cahyo Wibisono
#NIM : 2402053
#Kelas : RPL 1A

import time

# Array terurut
sorted_array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 
                32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 
                48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 
                74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]

# Linear Search
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# Binary Search
def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Pencarian dan perbandingan waktu
target = 60

# Linear Search Timing
start_linear = time.time()
linear_result = linear_search(sorted_array, target)
end_linear = time.time()
linear_time = end_linear - start_linear

# Binary Search Timing
start_binary = time.time()
binary_result = binary_search(sorted_array, target)
end_binary = time.time()
binary_time = end_binary - start_binary

# Hasil
print(f"Linear Search: indeks {linear_result}, waktu eksekusi {linear_time:.10f} detik")
print(f"Binary Search: indeks {binary_result}, waktu eksekusi {binary_time:.10f} detik")

# Kesimpulan
if linear_time < binary_time:
    print("Linear Search lebih cepat.")
else:
    print("Binary Search lebih cepat.")
