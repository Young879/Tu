#Nama : Dwi Cahyo Wibisono
#NIM : 2402053
#Kelas : RPL 1A




search = 20
array_list = [10, 55, 65, 25, 76, 87, 20, 75, 43]

def linear_search(search, array_list):
    for index, item in enumerate(array_list):
        if item == search:
            return index
    return -1

result = linear_search(search, array_list)
if result > 0:
    print(f'Ditemukan pada index ke {result}')
else:
    print('tidak ditemukan') 
