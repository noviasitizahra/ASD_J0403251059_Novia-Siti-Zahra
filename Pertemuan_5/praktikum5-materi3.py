# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ================================================
# Materi Rekursif : Menjumlahkan elemen list
# ================================================

def jumlah_list(data, index = 0):
    # base case
    if index == len(data):
        return 0
    
    # recursive case
    return data[index] + jumlah_list(data, index+1)

print("=== Program Jumlah Data ===")
print(jumlah_list([2,4,5,6,8]))