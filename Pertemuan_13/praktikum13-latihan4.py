# =====================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =====================================

# =============================================================
# Latihan 4. Studi Kasus: Jaringan Kabel Antar Gedung 
# Algoritma Prim untuk mencari biaya minimum pemasangan kabel
# =============================================================

import heapq   # modul heapq digunakan untuk priority queue (min-heap)

# Representasi weighted graph dengan dictionary
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

def prim(graph, start):
    visited = set([start])   # set untuk menyimpan gedung yang sudah terhubung
    edges = []               # priority queue untuk edge kandidat

    # Masukkan semua edge dari gedung awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []                 # list untuk menyimpan edge hasil MST
    total_cost = 0           # variabel untuk menghitung total biaya minimum

    # Proses pemilihan edge satu per satu
    while edges:
        weight, u, v = heapq.heappop(edges)   # ambil edge dengan bobot terkecil
        if v not in visited:                  # hanya dipilih jika gedung v belum terhubung
            visited.add(v)                    # tandai gedung v sudah terhubung
            mst.append((u, v, weight))        # tambahkan edge ke MST
            total_cost += weight              # tambahkan biaya ke total

            # Masukkan semua edge dari gedung v ke priority queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_cost

# Jalankan algoritma Prim mulai dari GedungA
mst, total = prim(graph, 'GedungA')

print("Jaringan Kabel Minimum (MST):")
for edge in mst:
    print(edge)   # tampilkan setiap edge yang terpilih

print("Total biaya minimum =", total)   # tampilkan total biaya minimum

# Pertanyaan Analisis:
# 1. Algoritma apa yang digunakan? 
# 2. Edge mana saja yang dipilih? 
# 3. Berapa total biaya minimum? 
# 4. Mengapa MST cocok digunakan pada kasus ini?

# Jawaban
# 1. Algoritma Prim, karena dimulai dari satu node lalu memilih edge terkecil
#    yang menghubungkan ke gedung baru.

# 2. - (GedungA, GedungC) = 2
#    - (GedungC, GedungD) = 1
#    - (GedungD, GedungB) = 3

# 3. Total biaya = 2 + 1 + 3 = 6

# 4. Karena MST memastikan semua gedung terhubung dengan biaya minimum
#    tanpa ada kabel yang berlebihan (tidak ada cycle).