# ==========================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================

# ========================================================== 
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota 
# Algoritma: Dijkstra 
# ========================================================== 

import heapq   # modul heapq dipakai untuk priority queue

# 1. Representasi graph berbobot menggunakan dictionary
# Key = kota, Value = tetangga dengan bobot (jarak/waktu)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},   # Bogor ke Jakarta 5, Bogor ke Depok 2
    'Depok': {'Jakarta': 2, 'Bandung': 6}, # Depok ke Jakarta 2, Depok ke Bandung 6
    'Jakarta': {'Bandung': 7},             # Jakarta ke Bandung 7
    'Bandung': {}                          # Bandung tidak punya tetangga
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    # Inisialisasi jarak semua kota = tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start = 0
    distances[start] = 0

    # 3. Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil kota dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak sekarang lebih besar dari jarak yang sudah tercatat, skip
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari kota sekarang
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # 4. Kembalikan hasil jarak terpendek dari start ke semua kota
    return distances

# 3. Input node awal (ditentukan langsung: Bogor)
hasil = dijkstra(graph, 'Bogor')

# 4. Output jarak terpendek dari Bogor ke semua kota
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# Pertanyaan Analisis
# 1. Node awal yang digunakan apa? 
# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# 3. Node mana yang memiliki jarak paling besar dari node awal? 
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. 

# Jawaban:
# 1. Node awal yang digunakan apa?
#    -> Node awal = Bogor
#
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    -> Depok, dengan jarak 2
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    -> Bandung, dengan jarak 8
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    -> Algoritma Dijkstra mulai dari Bogor dengan jarak 0.
#       Lalu memeriksa semua tetangga (Jakarta dan Depok).
#       Jarak ke Depok = 2, ke Jakarta = 5.
#       Karena Depok lebih dekat, diproses dulu.
#       Dari Depok ke Jakarta = 2 + 2 = 4 (lebih kecil daripada 5, jadi update).
#       Dari Depok ke Bandung = 2 + 6 = 8.
#       Dari Jakarta ke Bandung = 4 + 7 = 11 (lebih besar daripada 8, jadi tidak dipakai).
#       Hasil akhir: Bogor->Depok=2, Bogor->Jakarta=4, Bogor->Bandung=8.
