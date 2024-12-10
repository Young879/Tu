# Membuat file dummy data
with open("nilai_siswa.txt", "w") as file:
    data = [
        "Ali: 80", "Budi: 70", "Citra: 85", "Dina: 90", "Eka: 75",
        "Fajar: 88", "Gita: 78", "Hadi: 92", "Indah: 89", "Joko: 76",
        "Kiki: 84", "Lina: 81", "Mira: 87", "Nina: 79", "Omar: 91",
        "Putu: 73", "Qori: 77", "Rina: 88", "Sandi: 80", "Tio: 95"
    ]
    file.write("\n".join(data))

# Membaca file dan menghitung rata-rata
with open("nilai_siswa.txt", "r") as file:
    lines = file.readlines()
    total_nilai = 0
    jumlah_siswa = 0
    
    for line in lines:
        nama, nilai = line.strip().split(": ")
        total_nilai += int(nilai)
        jumlah_siswa += 1
    
    rata_rata = total_nilai / jumlah_siswa
    print(f"Nilai rata-rata dari {jumlah_siswa} siswa adalah: {rata_rata}")
