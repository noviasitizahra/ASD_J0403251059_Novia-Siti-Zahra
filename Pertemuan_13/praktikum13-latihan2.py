# =====================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =====================================

# ===========================================
# Latihan 2 . Implementasi Algoritma Kruskal
# Implementasi Sederhana Algoritma Kruskal 
# ===========================================

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 

# Mengurutkan edge berdasarkan bobot terkecil (ascending)
edges.sort()    # hasil: [(1,'C','D'), (2,'A','C'), (3,'B','D'), (4,'A','B'), (5,'A','D')]

mst = []            # list untuk menyimpan edge yang terpilih ke MST
total_weight = 0    # variabel untuk menghitung total bobot MST

connected = set()   # set untuk menyimpan vertex yang sudah terhubung

# Proses pemilihan edge satu per satu
for weight, u, v in edges: 
    # Memilih edge yang tidak membentuk cycle sederhana
    # logika sederhana: jika salah satu node belum ada di 'connected'
    if u not in connected or v not in connected: 

        mst.append((u, v, weight))  # tambahkan edge ke MST
        total_weight += weight      # tambahkan bobot edge ke total bobot

        connected.add(u)    # tandai node u sudah terhubung
        connected.add(v)    # tandai node v sudah terhubung

# Menampilkan hasil MST
print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge)     # tampilkan setiap edge yang terpilih

# Menampilkan total bobot MST
print("Total bobot =", total_weight)

# Pertanyaan Analisis
# 1. Edge mana yang dipilih pertama kali? 
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
# 3. Berapa total bobot MST yang dihasilkan? 
# 4. Mengapa edge tertentu tidak dipilih? 

# Jawaban
# 1. Edge dengan bobot paling kecil yaitu (1, 'C', 'D').
#    Karena Kruskal selalu mulai dari edge dengan bobot terkecil.

# 2. Prinsip algoritma Kruskal adalah greedy: selalu memilih edge dengan bobot terkecil yang tidak membentuk cycle.
#    Dengan cara ini, total bobot spanning tree akan minimum.

# 3. Edge yang dipilih:
#    (C, D) bobot 1
#    (A, C) bobot 2
#    (B, D) bobot 3
#    Total bobot = 1 + 2 + 3 = 6

# 4. Edge (A, B) bobot 4 dan (A, D) bobot 5 tidak dipilih karena:
#    Jika ditambahkan, akan membentuk cycle (lingkaran) dalam graph.
#    Kruskal hanya memilih edge yang menjaga spanning tree tetap terhubung tanpa cycle.