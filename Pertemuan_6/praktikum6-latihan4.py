# =======================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# =======================================

# =======================================
# Latihan 4 : Memahami Kode Program (Merge Sort)  
# =======================================

def merge_sort(data): 
    if len(data) <= 1: 
        return data 
     
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right) 
     
    return merge(left_sorted, right_sorted)

'''
Soal: 
1. Apa yang dimaksud dengan base case? 
Jawab: Base case itu kondisi berhenti dari rekursi
       Di sini kalau panjang data cuma 1 atau kurang (len(data) <= 1)
       berarti sudah terurut dan tidak perlu dipecah lagi

2. Mengapa fungsi memanggil dirinya sendiri? 
Jawab: Karena merge sort pakai konsep rekursi
        Data dipecah jadi dua bagian terus dipanggil lagi fungsi
        yang sama sampai datanya kecil banget (1 elemen)

3. Apa tujuan fungsi merge()? 
Jawab: Fungsi merge() buat menggabung dua list yang sudah terurut jadi satu list yang tetap terurut

'''