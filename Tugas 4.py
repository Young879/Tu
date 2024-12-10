#Nama : Dwi Cahyo Wibisono
#NIM : 2402053
#Kelas : RPL 1A



daftar_mahasiswa = ["Ali", "Budi", "Citra", "Dewi", "Eka", 
                    "Fajar", "Gina", "Hana", "Indra", "Joko", 
                    "Kiki", "Lia", "Mira", "Nina", "Oscar", 
                    "Putri", "Qori", "Rian", "Sari", "Toni"]

# Program pencarian mahasiswa
def cari_mahasiswa(daftar, nama):
    for mahasiswa in daftar:
        if mahasiswa.lower() == nama.lower():
            return f"{nama} terdaftar di Prodi RPL."
    return f"{nama} tidak terdaftar di Prodi RPL."

# Input pengguna
nama_dicari = input("Masukkan nama mahasiswa yang ingin dicari: ")
print(cari_mahasiswa(daftar_mahasiswa, nama_dicari))
