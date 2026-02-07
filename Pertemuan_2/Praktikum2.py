# =====================================================
# PRAKTIKUM 2 : KONSEP ADT DAN FILE HANDLING (STUDI KASUS)
# Latihan Dasar 1 : MEMBUAT FUNGSI LOAD DATA
# =====================================================
nama_file = "data_mahasiswa.txt"

# membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {} # Buat variabel untuk dictionary
    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # menghilang karakter baris baru
            parts = baris.split(",")
            if len(parts) != 3:
                continue
            nim, nama, nilai_str = parts
            nilai_int = int(nilai_str)
            nim, nama, nilai = baris.split(",") # pecah menjadi data satuan

            # simpan data mahasiswa ke dictionary dengan key NIM 
            data_dict[nim] = {      # KEY
                "nama": nama,       # VALUES
                "nilai": int(nilai) #VALUES
            }
    return data_dict

# memanggil fungsi baca_data_mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
# print("Jumlah data terbaca ", len(buka_data))

# =====================================================
# PRAKTIKUM 1 : KONSEP ADT DAN FILE HANDLING (STUDI KASUS)
# Latihan Dasar 2 : MEMBUAT FUNGSI MENAMPILKAN DATA
# =====================================================
def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print("Data kosong")
        return
    
    # membuat header tabel
    print("\n===== Daftar Mahasiswa =====")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    print("-" * 32) # Membuat garis header

    '''
    untuk tampilan yang rapi, atur f-string formating
        {'NIM' : <10} artinya:
        tampilkan nim <= rata kiri dengan lebar 10 karakter
        {'Nama': <12}
        tampilkan nama rata kiri, dengan lebar kolom 12 karakter
        {'Nilai': >5}
        tampilkan nilal => rata kanan, lebar kolom 5 karakter
    '''

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama: <12} | {nilai: >5}")

# tampilkan_data(buka_data)

# =====================================================
# PRAKTIKUM 2 : KONSEP ADT DAN FILE HANDLING (STUDI KASUS)
# Latihan Dasar 3 : MEMBUAT FUNGSI MENCARI DATA
# =====================================================
def cari_data(data_dict):
    # mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n===== Data mahasiswa ditemukan =====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("\nData tidak ditemukan")
        
# cari_data(buka_data)

# =====================================================
# PRAKTIKUM 2 : KONSEP ADT DAN FILE HANDLING (STUDI KASUS)
# Latihan Dasar 4 : MEMBUAT FUNGSI UPDATE NILAI
# =====================================================
def update_nilai(data_dict):
    # cari nim mahasiswa yang akan diupdate nilainya
    nim = input("Masukkan NIM mahasiswa yang akan diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0 - 100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. update dibatalkan ")

    nilai_lama = data_dict[nim]["nilai"]

    data_dict[nim]["nilai"] = nilai_baru
    # memasukkan nilai update baru ke dictionary
    print(f"Update berhasil, Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# update_nilai(buka_data)

# =====================================================
# PRAKTIKUM 2 : KONSEP ADT DAN FILE HANDLING (STUDI KASUS)
# Latihan Dasar 5 : MEMBUAT FUNGSI MENYIMPAN PERUBAHAN DATA KE FILE
# =====================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file,"w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}\n")

# simpan_data(nama_file, buka_data)
    print("Data berhasil disimpan")

# =====================================================
# PRAKTIKUM 2 : KONSEP ADT DAN FILE HANDLING (STUDI KASUS)
# Latihan Dasar 5 : MEMBUAT FUNGSI MENYIMPAN PERUBAHAN DATA KE FILE
# =====================================================

# fungsi 'main' program yg akan dijalankan terlebih dahulu
def main():

    # menjalankan fungsi 1 load data 
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n === MENU DATA MAHASISWA ===")
        print("1. Tampilkan semua data") # fungsi nomor 2
        print("2. Cari data berdasarkan NIM") 
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan")
        elif pilihan == "0":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid. COBA LAGI")

if __name__ == "__main__":
    main()