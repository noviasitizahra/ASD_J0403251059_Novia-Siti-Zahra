# =======================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# =======================================

# =======================================
# Latihan 3 : Tracing Insertion Sort  
# =======================================

# program insertion sort tracing
def insertion_sort(data):

    # melihat data awal
    print("Data awal: ", data)
    print("="*50)

    # loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] # simpan nilai yang disisipkan
        j = i-1 # index elemen terakhir di bagian kiri

        print("Iterasi ke- ", i)
        print("Nilai key: ", key)
        print("Bagian kiri (terurut): ", data[:i])
        print("Bagian kanan (belum terurut): ", data[i:])

        # geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

        # sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan: ", data)
        print("="*50)

    return data
    
data = [5, 2, 4, 6, 1, 3] 
print("Hasil sorting: ", insertion_sort(data))


'''
Buat program dengan menggunakan algoritma insertion sort 
Tracing dengan  data = [5, 2, 4, 6, 1, 3] 
 
Soal: 
 
1. Tuliskan isi list setelah iterasi i = 1. 
Jawab: 
Iterasi ke-  1
Nilai key:  2
Bagian kiri (terurut):  [5]
Bagian kanan (belum terurut):  [2, 4, 6, 1, 3]    
Setelah disisipkan:  [2, 5, 4, 6, 1, 3]

2. Tuliskan isi list setelah iterasi i = 3. 
Jawab: 
Iterasi ke-  3
Nilai key:  6
Bagian kiri (terurut):  [2, 4, 5]
Bagian kanan (belum terurut):  [6, 1, 3]
Setelah disisipkan:  [2, 4, 5, 6, 1, 3]

3. Berapa kali pergeseran terjadi pada iterasi i = 4? 
Jawab: angka 1 dibandingkan dengan: 
        6 -> geser 
        5 -> geser 
        4 -> geser
        2 -> geser 
    total pergeseran 4 kali 

'''