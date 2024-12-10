import csv

# Membuat file dummy data
with open("inventaris_barang.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nama Barang", "Jumlah"])
    data = [
        ["Pensil", 50], ["Pulpen", 60], ["Penghapus", 40],
        ["Buku Tulis", 30], ["Spidol", 20],
        ["Penggaris", 25], ["Kertas", 100],
        ["Stapler", 15], ["Binder", 35], ["Map", 50],
        ["Klip Kertas", 120], ["Amplop", 80], ["Gunting", 10],
        ["Kalkulator", 5], ["Tas Kerja", 12],
        ["Lem", 18], ["Lakban", 22], ["Tipe-X", 40],
        ["Sticky Note", 90], ["Folder", 32]
    ]
    writer.writerows(data)

# Fungsi untuk update stok
def update_stok(nama_barang, jumlah_perubahan):
    with open("inventaris_barang.csv", mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
    
    with open("inventaris_barang.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        
        for row in rows:
            if row[0] == nama_barang:
                row[1] = str(int(row[1]) + jumlah_perubahan)
            writer.writerow(row)

# Contoh penggunaan
update_stok("Pensil", -10)  # Mengurangi stok Pensil sebanyak 10
update_stok("Pulpen", 20)   # Menambah stok Pulpen sebanyak 20

# Menampilkan stok akhir
with open("inventaris_barang.csv", mode="r") as file:
    print(file.read())
