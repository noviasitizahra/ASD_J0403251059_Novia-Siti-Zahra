# ==========================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================

# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ========================================================== 

# Representasi weighted graph menggunakan dictionary bersarang 
# Key = node, Value = tetangga dengan bobot (jarak)
graph = { 
    'A': {'B': 4, 'C': 2},   # dari A ke B bobot 4, ke C bobot 2
    'B': {'D': 5},           # dari B ke D bobot 5
    'C': {'D': 1},           # dari C ke D bobot 1
    'D': {}                  # D tidak punya tetangga
} 

# Menghitung dua kemungkinan jalur dari A ke D 
# Jalur 1: A -> B -> D
jalur_1 = graph['A']['B'] + graph['B']['D']     # bobot A-B ditambah bobot B-D

# Jalur 2: A -> C -> D
jalur_2 = graph['A']['C'] + graph['C']['D']     # bobot A-C ditambah bobot C-D

# Cetak hasil perhitungan bobot masing-masing jalur
print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

# Bandingkan kedua jalur untuk menentukan jalur terpendek
if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D") 

# Pertanyaan Analisis 
# 1. Berapa total bobot jalur A -> B -> D? 
# 2. Berapa total bobot jalur A -> C -> D? 
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit? 

# Jawaban:
# 1. Dari A ke B = 4
#    Dari B ke D = 5
#    Total = 4 + 5 = 9

# 2. Dari A ke C = 2
#    Dari C ke D = 1
#    Total = 2 + 1 = 3

# 3. Jalur A → C → D dengan bobot 3
# Karena 3 lebih kecil daripada 9, maka jalur ini yang dipilih sebagai jalur terpendek.

# 4. Karena yang dihitung adalah total bobot (weight), bukan jumlah edge.
# Bisa saja jalur dengan edge lebih sedikit punya bobot lebih besar.
# Contoh di kasus ini:
# Jalur A → B → D hanya punya 2 edge, tapi total bobotnya 9.
# Jalur A → C → D juga punya 2 edge, tapi total bobotnya 3.
# Jadi, jalur terpendek ditentukan oleh jumlah bobot terkecil, bukan jumlah edge.

