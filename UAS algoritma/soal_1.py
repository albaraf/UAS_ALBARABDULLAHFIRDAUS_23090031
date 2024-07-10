mahasiswa = []

while True:
    print("Program Daftar Mahasiswa")

    nim = input("Masukan NIM: ")

    nama = input("Masukan Nama: ")

    mahasiswa.append({"NIM": nim, "Nama": nama})

    tambah_lagi = input("Ingin tambah lagi? (YA/TIDAK): ")

    if tambah_lagi.upper() != "YA":
        break

print("Data Mahasiswa:")
for i, data in enumerate(mahasiswa, start=1):
    print(f"{i}. NIM: {data['NIM']}, Nama: {data['Nama']}")

print("Program selesai.")