# ==========================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==========================================

# ==========================================
# materi 2 : Algoritma Bellman Ford 
# ==========================================

graph = {
    'A' : {'B' : 4, 'C' : 2},
    'B' : {'D' : 5},
    'C' : {'D' : 1},
    'D' : {}
}

def bellman_ford(graph, start): 
    # Inisialisasi jarak: semua node dianggap tak terhingga (inf)
    distances = {node: float('inf') for node in graph} 
    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0 
 
    # Relaksasi berulang sebanyak (jumlah node - 1) kali
    # Tujuannya: memastikan semua jalur terpendek ditemukan
    for _ in range(len(graph) - 1): 
 
        # Periksa setiap node dalam graph
        for node in graph: 
 
            # Periksa semua tetangga dari node tersebut
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak melalui node sekarang lebih kecil
                if distances[node] + weight < distances[neighbor]: 
                    # Update jarak ke tetangga dengan jarak baru
                    distances[neighbor] = distances[node] + weight 

    # Kembalikan hasil jarak terpendek dari node awal ke semua node
    return distances

print(bellman_ford(graph, 'A'))