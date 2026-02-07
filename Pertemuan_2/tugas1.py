# ============================================================
# PRAKTIKUM 1: ADT & FILE HANDLING (STUDI KASUS: DATA BARANG)
# LATIHAN : MENU INTERAKTIF 
# ============================================================

nama_file = "data_barang.txt"

# ------------------------------
# 1) Read: baca data dari file
# ------------------------------

def baca_data_barang(nama_file):
    """
    membaca data mahasiswa dari file
    format per baris: kode, nama, stok

    output:
    - data dict (dictionary)
        key = kode
        value = {"Nama barang": nama, "Stok": stok(int)}
    """
    data_dict = {}

    # jika file belum ada, kembalikan dictionary kosong (aman)
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                # lewati baris kosong
                if baris == "":
                    continue

                parts = baris.split(",")
                if len(parts) != 3:
                    continue

                kode, nama, stok_str = parts

                try:
                    stok_int = int(stok_str)
                except ValueError:
                    continue
                data_dict[kode] = {"nama": nama, "stok": stok_int}
            
    except FileNotFoundError:
        # file tidak ditemukan -> data kosong
        pass

    return data_dict

# ------------------------------
# 2) tampilkan semua data
# ------------------------------
def tampilkan_semua_barang(data_dict):
    """
    menampilkan semua data barang dalam format tabel
    """
    if len(data_dict) == 0:
        print("Data barang kosong")
        return
    
    print("\n=== DATA BARANG ===")
    print(f"{'Kode Barang': <10} | {'Nama': <12} | {'Stok': >5}")
    print("-" * 36)

    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["nama"]
        stok = data_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<12} | {stok:>5}")

# ---------------------------------------
# 3) cari barang berdasarkan kode barang
# ---------------------------------------
def cari_barang(data_dict):
    """
    mencari barang berdasarkan kode barang (key dictionary)
    """
    kode_cari = input("Masukkan kode barang yang ingin dicari: ").strip()

    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        stok = data_dict[kode_cari]["stok"]

        print("\n=== DATA BARANG DITEMUKAN ===")
        print(f"Kode Barang : {kode_cari}")
        print(f"Nama Barang : {nama}")
        print(f"Stok        : {stok}")
    else:
        print("\nBarang tidak ditemukan. Pastikan kode barang yang dimasukkan benar")

# ------------------------------
# 5) update stok barang
# ------------------------------
def tambah_barang_baru(data_dict):
    """
    menambahkan barang baru ke data barang
    """
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in data_dict:
        print("Kode sudah digunakan")
        return
    
    nama = input("Masukkan nama barang: ").strip()

    try:
        stok = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka")
        return
    
    if stok < 0 or stok > 100:
        print("Stok harus antara 0 sampai 100")
        return
    
    data_dict[kode] = {
        "nama": nama,
        "stok": stok
    }

    print("Barang baru berhasil ditambahkan")


# ------------------------------
# 5) update stok barang
# ------------------------------
def update_stok_barang(data_dict):
    """
    mengubah stok barang berdasarkan kode barang
    aturan:
    - kode barang harus ada
    - stok baru harus 0-100
    """
    kode = input("Masukkan kode barang yang ingin diupdate stoknya: ").strip()

    if kode not in data_dict:
        print("Kode barang tidak ditemukan. Update dibatalkan")
        return
    try:
        stok_baru = int(input("Masukkan stok baru (0-100): ").strip())
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan")
        return
    
    if stok_baru < 0 or stok_baru > 100:
        print("Stok harus antara 0 sampai 100. Update dibatalkan")
        return
    
    stok_lama = data_dict[kode]["stok"]
    data_dict[kode]["stok"] = stok_baru

    print(f"Update berhasil. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")

# ------------------------------
# 6) write: simpan data ke file
# ------------------------------
def simpan_data_barang(nama_file, data_dict):
    """
    menyimpan data barang dari dictionary ke file
    format per baris: kode_barang, nama_barang, stok
    """
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            stok = data_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

# ------------------------------
# menu interaktif
# ------------------------------
def main():
    # load data saat program dimulai
    data_barang = baca_data_barang(nama_file)

    while True:
        print("\n=== MENU DATA BARANG ===")
        print("1. tampilkan semua barang")
        print("2. cari barang berdasarkan kode barang")
        print("3. tambah barang baru")
        print("4. update stok barang")
        print("5. simpan data ke file")
        print("0. keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua_barang(data_barang)
        elif pilihan == "2":
            cari_barang(data_barang)
        elif pilihan == "3":
            tambah_barang_baru(data_barang)
        elif pilihan == "4":
            update_stok_barang(data_barang)
        elif pilihan == "5":
            simpan_data_barang(nama_file, data_barang)
            print("Data berhasil disimpan")
        elif pilihan == "0":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi")

if __name__ == "__main__":
    main()