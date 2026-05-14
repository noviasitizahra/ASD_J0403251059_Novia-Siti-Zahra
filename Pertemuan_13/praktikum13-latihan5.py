# =====================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =====================================

# ===========================================
# Latihan 5 . Tugas Mandiri: MST dengan Kasus Baru
# Kasus 1: Jaringan Jalan Antar Kota
# Algoritma Kruskal
# ===========================================

# Daftar edge: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Urutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []             # list untuk menyimpan edge MST
total_weight = 0     # total bobot MST
connected = set()    # set untuk menyimpan kota yang sudah terhubung

# Proses pemilihan edge
for weight, u, v in edges:
    # pilih edge jika salah satu kota belum terhubung (logika sederhana untuk hindari cycle)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))   # tambahkan edge ke MST
        total_weight += weight       # tambahkan bobot ke total
        connected.add(u)             # tandai kota u sudah terhubung
        connected.add(v)             # tandai kota v sudah terhubung

# Output MST
print("Minimum Spanning Tree (Jaringan Jalan):")
for edge in mst:
    print(edge)

# Output total bobot minimum
print("Total bobot minimum =", total_weight)

# Pertanyaan Analisis:
# 1. Kasus apa yang dipilih? 
# 2. Algoritma apa yang digunakan? 
# 3. Edge mana saja yang dipilih dalam MST? 
# 4. Berapa total bobot MST? 
# 5. Mengapa edge tertentu tidak dipilih?

# Jawaban
# 1. Kasus 1: Jaringan Jalan Antar Kota (Bogor, Jakarta, Depok, Bandung).

# 2. Algoritma Kruskal, karena memilih edge terkecil satu per satu tanpa cycle.

# 3. - (Bogor, Depok) = 2
#    - (Depok, Jakarta) = 3
#    - (Depok, Bandung) = 4

# 4. Total bobot = 2 + 3 + 4 = 9

# 5. Edge (Bogor, Jakarta)=5 dan (Jakarta, Bandung)=6 tidak dipilih
#    karena jika ditambahkan akan membentuk cycle, sehingga tidak efisien.