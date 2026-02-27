# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ================================================
# Latihan 4: Kombinasi huruf
# ================================================

def kombinasi(n, hasil=""):
    # base case
    # Jika panjang string sudah sama dengan n
    # maka cetak hasil kombinasi
    if len(hasil) == n:
        print(hasil)
        return
    
    # recursive case
    # tambahkan huruf "A" lalu panggil lagi fungsi
    kombinasi(n, hasil + "A")

    # tambahkan huruf "B" lalu panggil lagi fungsi
    kombinasi(n, hasil + "B")

# memanggil fungsi untuk panjang kombinasi 2
# karena setiap posisi ada 2 pilihan (A/B),
# maka jumlah kombinasi = 2^n
kombinasi(2)
