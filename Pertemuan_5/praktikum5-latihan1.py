# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ================================================
# Latihan 1: Rekursi pangkat
# ================================================

def pangkat(a, n):
    # base case
    # jika pangkat 0, maka hasilnya 1
    # karena dalam matematika a^0 = 1
    if n == 0:
        return 1
    
    # recursive case
    # fungsi memanggil dirinya sendiri dengan n dikurangi 1
    # artinya kita mengalikan a dengan hasil dari a^(n-1)
    return a * pangkat(a, n - 1)

# memanggil fungsi pangkat dengan nilai a=2 dan n=4
# prosesnya => 2 * 2 * 2 * 2
print(pangkat(2, 4)) # output: 16