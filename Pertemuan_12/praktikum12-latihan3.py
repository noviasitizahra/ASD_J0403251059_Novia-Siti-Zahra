# ==========================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================

# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 
 
# Weighted graph dengan bobot negatif 
# Key = node, Value = tetangga dengan bobot (jarak)
graph = { 
    'A': {'B': 5, 'C': 4},  # dari A ke B bobot 5, ke C bobot 4
    'B': {},                # B tidak punya tetangga
    'C': {'B': -2}          # dari C ke B bobot -2 (contoh bobot negatif)
} 
 
def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga (inf)
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
 
        # Periksa semua edge dalam graph
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    # Kembalikan hasil jarak terpendek dari start ke semua node
    return distances  
 
# Panggil fungsi Bellman-Ford mulai dari node 'A'
hasil = bellman_ford(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance) 

# Pertanyaan Analisis 
# 1. Berapa bobot langsung dari A ke B? 
# 2. Berapa total bobot jalur A -> C -> B? 
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
# 5. Apa yang dimaksud dengan proses relaksasi edge? 
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra? 

# Jawaban:
# 1. Bobot langsung A → B = 5

# 2. A → C = 4, lalu C → B = -2
#    Total = 4 + (-2) = 2

# 3. Jalur A → C → B dengan bobot 2 lebih kecil daripada jalur langsung A → B = 5

# 4. Karena Bellman-Ford melakukan relaksasi berulang kali, sehingga tetap bisa menemukan jalur terpendek meskipun ada edge berbobot negatif. 
# Algoritma ini tidak bergantung pada asumsi bobot positif seperti Dijkstra.

# 5.  Relaksasi adalah proses membandingkan jarak lama dengan jarak baru (melalui suatu edge). 
# Jika jarak baru lebih kecil, maka jarak lama diperbarui. Proses ini diulang berkali-kali sampai semua jalur terpendek ditemukan.

# 6. Dijkstra: hanya bisa digunakan untuk graph dengan bobot positif, lebih cepat karena pakai priority queue.
#    Bellman-Ford: bisa digunakan untuk graph dengan bobot negatif, tapi lebih lambat karena harus melakukan relaksasi sebanyak N-1 kali (N = jumlah node).