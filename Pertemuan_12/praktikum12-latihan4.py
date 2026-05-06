# ==========================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================

# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ========================================================== 

import heapq     # modul heapq dipakai untuk priority queue

# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
# Key = lokasi, Value = tetangga dengan bobot (waktu tempuh dalam menit)
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, # dari Gerbang ke Perpustakaan 6 menit, ke Kantin 2 menit
    'Perpustakaan': {'Lab': 3},                 # dari Perpustakaan ke Lab 3 menit
    'Kantin': {'Lab': 4, 'Aula': 7},            # dari Kantin ke Lab 4 menit, ke Aula 7 menit
    'Lab': {'Aula': 1},                         # dari Lab ke Aula 1 menit
    'Aula': {}                                  # Aula tidak punya tetangga
} 

def dijkstra(graph, start): 
    # Inisialisasi jarak semua lokasi = tak hingga
    distances = {node: float('inf') for node in graph} 
    # Jarak dari start ke start = 0
    distances[start] = 0 

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)] 

    while priority_queue: 
        # Ambil lokasi dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue) 

        # Jika jarak sekarang lebih besar dari jarak yang sudah tercatat, skip
        if current_distance > distances[current_node]: 
            continue 
        
        # Periksa semua tetangga dari lokasi sekarang
        for neighbor, weight in graph[current_node].items(): 
            # Hitung jarak baru
            distance = current_distance + weight 

            # Jika jarak baru lebih kecil, update
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                # Masukkan tetangga ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor)) 

    # Kembalikan hasil jarak terpendek dari start ke semua lokasi
    return distances 

# Panggil fungsi Dijkstra dari Gerbang    
hasil = dijkstra(graph, 'Gerbang') 

print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit")

# Pertanyaan Analisis 
# 1. Lokasi mana yang paling dekat dari Gerbang? 
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# Jawaban:
# 1. Kantin, dengan jarak 2 menit.

# 2. Jalur Gerbang → Kantin → Lab → Aula = 2 + 4 + 1 = 7 menit
#    Jalur Gerbang → Kantin → Aula langsung = 2 + 7 = 9 menit
#    Jalur Gerbang → Perpustakaan → Lab → Aula = 6 + 3 + 1 = 10 menit
#    → Jadi waktu tempuh terpendek = 7 menit.

# 3. Tidak. Jalur langsung bisa saja lebih panjang bobotnya. Contoh: Gerbang → Kantin → Aula langsung = 9 menit, 
# padahal lewat Kantin → Lab → Aula = 7 menit lebih cepat. Jadi jalur terpendek ditentukan oleh total bobot terkecil, bukan apakah jalurnya langsung atau tidak.

# 4. Karena semua bobot (waktu tempuh) bernilai positif, dan kita ingin mencari jalur tercepat dari satu lokasi ke lokasi lain. 
# Dijkstra efisien untuk kasus seperti ini, sehingga cocok dipakai untuk simulasi rute kampus.