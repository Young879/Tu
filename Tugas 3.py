#Nama : Dwi Cahyo Wibisono
#NIM : 2402053
#Kelas : RPL 1A


stok_barang = ["Sabun", "Shampoo", "Sikat Gigi", "Pasta Gigi", "Tisu", 
               "Masker", "Hand Sanitizer", "Sabun Cuci", "Deterjen", "Pewangi", 
               "Pembersih Lantai", "Kain Pel", "Spons", "Sapu", "Ember"]

# Program pencarian barang
def cari_barang(stok, barang):
    for item in stok:
        if item.lower() == barang.lower():
            return f"{barang} tersedia dalam stok."
    return f"{barang} tidak tersedia dalam stok."

# Input pengguna
barang_dicari = input("Masukkan nama barang yang ingin dicari: ")
print(cari_barang(stok_barang, barang_dicari))
