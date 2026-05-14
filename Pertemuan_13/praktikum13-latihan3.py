# =====================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =====================================

# ===========================================
# Latihan 3 . Implementasi Algoritma Prim 
# ===========================================

import heapq    # modul heapq digunakan untuk priority queue (min-heap)

# Representasi graph dengan dictionary bersarang
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5},  # node A terhubung ke B,C,D dengan bobot masing-masing
    'B': {'A': 4, 'D': 3},          # node B terhubung ke A,D
    'C': {'A': 2, 'D': 1},          # node C terhubung ke A,D
    'D': {'A': 5, 'B': 3, 'C': 1}   # node D terhubung ke A,B,C
} 

def prim(graph, start): 

    visited = set([start])  # set untuk menyimpan node yang sudah dikunjungi, awalnya hanya start
    edges = []              # priority queue untuk menyimpan edge kandidat

    # Masukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 

    mst = []            # list untuk menyimpan edge hasil MST
    total_weight = 0    # variabel untuk menghitung total bobot MST

    # Proses pemilihan edge satu per satu
    while edges:
        weight, u, v = heapq.heappop(edges)     # ambil edge dengan bobot terkecil
        if v not in visited:                    # hanya dipilih jika node v belum dikunjungi
            
            visited.add(v)               # tandai node v sudah dikunjungi
            mst.append((u, v, weight))   # tambahkan edge ke MST
            total_weight += weight       # tambahkan bobot ke total

            # Masukkan semua edge dari node v ke priority queue
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
    return mst, total_weight 

# Jalankan algoritma Prim mulai dari node A
mst, total = prim(graph, 'A') 

print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge)     # tampilkan setiap edge yang terpilih

print("Total bobot =", total)   # tampilkan total bobot MST

# Pertanyaan Analisis:
# 1. Node awal apa yang digunakan? 
# 2. Edge mana yang dipilih pertama kali? 
# 3. Bagaimana Prim menentukan edge berikutnya? 
# 4. Berapa total bobot MST yang dihasilkan? 
# 5. Apa perbedaan pendekatan Prim dan Kruskal? 

# Jawaban
# 1. Node awal adalah A (sesuai parameter fungsi prim).

# 2. Edge (A, C) dengan bobot 2, karena bobotnya paling kecil dari node A.

# 3. Prim selalu memilih edge dengan bobot terkecil dari node yang sudah terhubung
#    ke node yang belum dikunjungi, menggunakan priority queue.

# 4. Edge terpilih: (A,C)=2, (C,D)=1, (D,B)=3
#    Total bobot = 2 + 1 + 3 = 6

# 5. - Prim: mulai dari satu node, lalu menambah edge terkecil yang menghubungkan
#      node visited ke node baru (berbasis node).
#    - Kruskal: mengurutkan semua edge, lalu memilih edge terkecil satu per satu
#      tanpa membentuk cycle (berbasis edge).