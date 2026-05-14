# =====================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =====================================

# ===========================================
# Latihan 1 .  Memahami Konsep Spanning Tree 
# ===========================================

# Daftar edge graph 
edges = [ 
    ('A', 'B'), 
    ('A', 'C'), 
    ('A', 'D'), 
    ('C', 'D'), 
    ('B', 'D') 
] 

# Contoh spanning tree 
spanning_tree = [ 
    ('A', 'C'), 
    ('C', 'D'), 
    ('D', 'B') 
] 

print("Edge pada graph:") 
for edge in edges: 
    print(edge) 

print("\nSpanning Tree:") 

for edge in spanning_tree: 
    print(edge) 

print("\nJumlah edge graph =", len(edges)) 
print("Jumlah edge spanning tree =", len(spanning_tree)) 

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