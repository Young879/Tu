#Nama : Dwi Cahyo Wibisono
#NIM : 2402053
#Kelas : RPL 1A




arr = [8, 9, 10, 19, 20, 22, 43, 55, 67, 91]
nilai = 91

def binary_search(nilai, array_list):
    left = 0
    right = len(array_list) -1 
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == nilai:
            return mid
        elif nilai > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

result = binary_search(nilai, arr)
print(f"pencarian 23: {result}")