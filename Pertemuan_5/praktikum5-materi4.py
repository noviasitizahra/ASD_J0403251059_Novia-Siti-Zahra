# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ================================================
# Contoh Backtracking 1 : Kombinasi biner (n)
# ================================================

def biner(n, hasil=""):
    # base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # choose + explore: tambah '0'
    biner(n, hasil + "0")

    # chose + explore: tambah '1'
    biner(n, hasil + "1")

biner(3)