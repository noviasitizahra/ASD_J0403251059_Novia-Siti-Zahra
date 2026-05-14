# =====================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =====================================

# ===========================================
# Latihan 1 .  Memahami Konsep Spanning Tree 
# ===========================================

# Daftar edge graph (menyimpan semua sisi/edge dari graph awal)
edges = [ 
    ('A', 'B'),     # edge antara vertex A dan B
    ('A', 'C'),     # edge antara vertex A dan C
    ('A', 'D'),     # edge antara vertex A dan D
    ('C', 'D'),     # edge antara vertex C dan D
    ('B', 'D')      # edge antara vertex B dan D
] 

# Contoh spanning tree (subgraph yang mencakup semua vertex tanpa cycle)
spanning_tree = [ 
    ('A', 'C'),     # edge menghubungkan A ke C
    ('C', 'D'),     # edge menghubungkan C ke D
    ('D', 'B')      # edge menghubungkan D ke B
] 

# Menampilkan semua edge pada graph awal
print("Edge pada graph:") 
for edge in edges:  # loop untuk menampilkan setiap edge
    print(edge) 

# Menampilkan edge pada spanning tree
print("\nSpanning Tree:") 
for edge in spanning_tree:  # loop untuk menampilkan setiap edge spanning tree
    print(edge) 

# Menampilkan jumlah edge pada graph awal
print("\nJumlah edge graph =", len(edges))  # menghitung panjang list edges

# Menampilkan jumlah edge pada spanning tree
print("Jumlah edge spanning tree =", len(spanning_tree))    # menghitung panjang list spanning_tree

# Pertanyaan Analisis
# 1. Apa perbedaan graph awal dan spanning tree? 
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 

# Jawaban
# 1. - Graph awal bisa memiliki cycle dan jumlah edge lebih banyak.
#    - Spanning tree adalah subgraph yang mencakup semua vertex, terhubung, tetapi tidak memiliki cycle.

# 2. Karena spanning tree harus berbentuk pohon (tree),
#    dan definisi tree adalah graph terhubung tanpa cycle.

# 3. Karena spanning tree hanya membutuhkan jumlah edge = jumlah vertex - 1.
#    Jika lebih banyak, pasti terbentuk cycle.