# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ================================================
# Studi kasus: generator PIN
# ================================================

def buat_pin(panjang, hasil=""):
    # base case
    # jika panjang string sudah sesuai dengan panjang PIN
    # maka cetak PIN tersebut
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # loop untuk setiap kemungkinan angka
    # di sini pilihannya adalah 0, 1, dan 2
    for angka in ["0", "1", "2"]:
        # cek dulu apakah angka sudah ada di dalam hasil
        # jika belum ada, baru lanjut rekursi
        if angka not in hasil:
        # recursive call
        # tambahkan angka ke hasil lalu panggil fungsi lagi
            buat_pin(panjang, hasil + angka)

# memanggil fungsi untuk membuat PIN sepanjang 3 digit
# karena setiap digit punya 3 pilihan,
# maka jumlah kombinasi = 3^panjang
buat_pin(3)