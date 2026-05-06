# ==========================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================

# ========================================================== 
# Latihan 2: Implementasi Dijkstra 
# ========================================================== 

import heapq    # modul heapq dipakai untuk priority queue (antrian dengan prioritas)

# Weighted graph dengan bobot positif 
# Key = node, Value = tetangga dengan bobot (jarak)
graph = { 
    'A': {'B': 4, 'C': 2},  # dari A ke B bobot 4, ke C bobot 2
    'B': {'D': 5},          # dari B ke D bobot 5
    'C': {'D': 1},          # dari C ke D bobot 1
    'D': {}                 # D tidak punya tetangga
} 

def dijkstra(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    """ 
    # Semua jarak awal dibuat tak hingga (inf)
    distances = {node: float('inf') for node in graph} 

    # Jarak dari start ke start adalah 0 
    distances[start] = 0 

    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)] 

     # Selama queue tidak kosong
    while priority_queue: 
        # Ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 
 
        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            # Hitung jarak baru = jarak sekarang + bobot edge
            distance = current_distance + weight 
 
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                # Update jarak minimum
                distances[neighbor] = distance 
                # Masukkan tetangga ke priority queue dengan jarak barunya
                heapq.heappush(priority_queue, (distance, neighbor)) 
    
    # Kembalikan hasil jarak minimum ke semua node
    return distances 
 
# Panggil fungsi Dijkstra mulai dari node 'A' 
hasil = dijkstra(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance) 

# Pertanyaan Analisis 
# 1. Berapa jarak terpendek dari A ke B? 
# 2. Berapa jarak terpendek dari A ke C? 
# 3. Berapa jarak terpendek dari A ke D? 
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif? 

# Jawaban:
# 1. Jarak A → B = 4
# 2. Jarak A → C = 2
# 3. Jalur A → C → D = 2 + 1 = 3 (lebih pendek daripada A → B → D = 9)
# 4. Karena bobot jalur lewat C (2 + 1 = 3) lebih kecil daripada bobot jalur lewat B (4 + 5 = 9). Jadi meskipun sama-sama 2 edge, total bobotnya berbeda.
# 5. Priority queue memastikan node dengan jarak paling kecil diproses lebih dulu. Ini penting supaya algoritma selalu memperluas jalur terpendek terlebih dahulu.
# 6. Karena Dijkstra mengasumsikan sekali jarak terpendek ditemukan, tidak akan berubah lagi. Jika ada bobot negatif, 
# asumsi ini rusak, jalur bisa jadi lebih pendek setelah melewati edge negatif. Untuk kasus bobot negatif, algoritma Bellman-Ford lebih tepat digunakan.