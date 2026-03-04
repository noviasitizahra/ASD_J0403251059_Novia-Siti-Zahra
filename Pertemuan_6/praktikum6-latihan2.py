# =======================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# =======================================

# =======================================
# Latihan 2 : Melengkapi Potongan Kode 
# =======================================
'''
SOAL: 

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and ______________________: 
            data[j + 1] = data[j] 
            j -= 1 
         
        ______________________ 
     
    return data 
'''

'''
Soal: 
1. Lengkapi kondisi agar menjadi sorting ascending. 
Jawab: 
'''
# sorting ascending
def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j+1] = key
    return data 

'''
2. Ubah agar menjadi descending. 
Jawab: 
'''
# sorting descending
def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] < key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j+1] = key
    return data 

