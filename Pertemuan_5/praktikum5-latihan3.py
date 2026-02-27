# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ================================================
# Latihan 3: Mencari nilai maksimum
# ================================================

def cari_maks(data, index=0):
    # base case
    # jika index sudah di elemen terakhir
    # maka langsung kembalikan nilai tersebut
    if index == len(data) - 1:
        return data[index]
    
    # recursive case
    # cari nilai maksimum dari sisa elemen setelah index sekarang
    maks_sisa = cari_maks(data, index + 1)

    # bandingkan elemen sekarang dengan maksimum dari sisa elemen
    if data[index] > maks_sisa:
        return data[index]  # jika lebih besar, kembalikan nilai sekarang
    else:
        return maks_sisa    # jika tidak, kembalikan maksimum dari sisa

# data yang akan dicari nilai maksimumnya    
angka = [3, 7, 2, 9, 5]

# menampilkan hasil
print("Nilai maksimum:", cari_maks(angka))