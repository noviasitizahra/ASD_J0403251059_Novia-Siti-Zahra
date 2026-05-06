# ==========================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==========================================

# ==========================================
# materi 1 : Algoritma Dijkstra 
# ==========================================

import heapq    # modul heapq dipakai untuk membuat priority queue (antrian dengan prioritas)

# Struktur graph: tiap node punya tetangga dengan bobot (jarak)
graph = {
    'A' : {'B' : 4, 'C' : 2},   # dari A ke B jaraknya 4, ke C jaraknya 2
    'B' : {'D' : 5},            # dari B ke D jaraknya 5
    'C' : {'D' : 1},            # dari C ke D jaraknya 1
    'D' : {}                    # D tidak punya tetangga
} 

def dijkstra(graph, start):
    # menyimpan jarak minimum dari node awal ke semua node
    # awalnya semua jarak dianggap tak terhingga (inf)
    distances = {node: float('inf') for node in graph}

    # jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # priority queue berisi pasangan (jarak, node)
    # mulai dari node awal dengan jarak 0
    pq = [(0, start)]

    # selama masih ada isi di priority queue
    while pq:
        # ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(pq)

        # periksa semua tetangga dari node sekarang
        for neighbor, weight in graph[current_node].items():

            # hitung jarak baru = jarak sekarang + bobot edge
            distance = current_distance + weight

            # jika jarak baru lebih kecil dari jarak lama
            if distance < distances[neighbor]:
                # update jarak minimum
                distances[neighbor] = distance

                # masukkan tetangga ke priority queue dengan jarak barunya
                heapq.heappush(pq, (distance, neighbor))

    # kembalikan hasil jarak minimum ke semua node
    return distances

# panggil fungsi Dijkstra mulai dari node 'A'
hasil = dijkstra(graph, 'A')
print(hasil)    # hasil berupa dictionary jarak minimum dari A ke semua node