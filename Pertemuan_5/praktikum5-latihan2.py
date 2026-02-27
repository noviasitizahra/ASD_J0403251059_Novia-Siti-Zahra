# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ================================================
# Latihan 2: Tracing rekursi
# ================================================

def countdown(n):
    # base case
    # jika n sudah 0, hentikan rekursi
    if n == 0:
        print("Selesai") # tanda bahwa rekursi sudah sampai akhir
        return          # menghentikan fungsi
    
    # cetak sebelum masuk ke rekursi (fase turun / descending)
    print("Masuk:", n)

     # recursive call
     # memanggil fungsi dengan n dikurangi 1
    # fungsi akan terus dipanggil sampai n == 0
    countdown(n-1)

    # baris ini dijalankan setelah rekursi selesai
    # karena sistem stack, maka urutannya jadi terbalik
    print("Keluar:", n)

# memulai countdown dari 3
countdown(3)