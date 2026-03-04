# =======================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# =======================================

# =======================================
# Latihan 1 : Memahami Kode Program (Insertion Sort)
# =======================================

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data 

'''
Soal: 
1. Mengapa perulangan dimulai dari indeks 1? 
Jawab: karena indeks 0 itu dianggap sudah terurut sendirinya, jadi kita mulai dari indeks 1
       buat dibandingin sama elemen sebelumnya, insertion sort itu konsepnya
       seperti nyusun kartu, kita ambil satu kartu lalu masukin ke posisi yang
       benar di bagian yang sudah tersusun

2. Apa fungsi variabel key? 
Jawab: itu untuk menyimpan sementara nilai yang lagi mau diposisikan dengan benar,
       jadi agar nilainya tidak hilang waktu elemen lain digeser-geser

3. Mengapa digunakan while, bukan for? 
Jawab: karena kita belum tahu berapa kali harus mundur untuk cari posisi yang pas,
       jadi pakai while supaya bisa terus mengecek selama kondisi masih terpenuhi,
       misalnya masih ada angka yang lebih besar dari key    

4. Operasi apa yang terjadi di dalam while? 
Jawab: di dalam while terjadi proses pergeseran elemen, kalau ada angka yang lebih besar dari key,
       maka angka itu digeser ke kanan supaya nanti key bisa masuk ke posisi yang benar

'''