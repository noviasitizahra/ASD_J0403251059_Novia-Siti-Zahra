# =======================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# =======================================

# =======================================
# Latihan 5 : Melengkapi Fungsi Merge   
# =======================================
'''
SOAL : 
def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
     
    while i < len(left) and j < len(right): 
        if __________________________: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
     
    result.extend(left[i:]) 
    result.extend(right[j:]) 
     
    return result
'''

'''
Soal: 
1. Lengkapi kondisi agar menjadi ascending. 
Jawab: 
'''
# kondisi ascending
def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
     
    while i < len(left) and j < len(right): 
        if left[i] <= right[j]:
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
     
    result.extend(left[i:]) 
    result.extend(right[j:]) 
     
    return result


'''
2. Jelaskan fungsi result.extend(). 
Jawab: result.extend() itu buat nambahin sisa elemen yang belum masuk ke dalam list result
        Misalnya salah satu list sudah habis duluan, maka sisa list yang lain langsung ditambahin semua ke result
        Jadi tidak ada elemen yang kelewat
'''