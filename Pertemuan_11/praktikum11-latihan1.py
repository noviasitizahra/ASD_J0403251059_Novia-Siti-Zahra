# ==================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==================================

# ====================================================
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
# ====================================================

# Sebuah graph digunakan untuk merepresentasikan hubungan antar lokasi sebagai berikut: 
# Struktur graph dalam bentuk dictionary
# Key = nama lokasi, Value = daftar lokasi yang terhubung langsung
graph = {
    'Rumah' : ['Sekolah', 'Toko'],
    'Sekolah' : ['Perpustakaan'],
    'Toko' : ['Pasar'],
    'Perpustakaan' : [],
    'Pasar' : []
}

# Graph tersebut menggambarkan jalur dari Rumah ke lokasi lain. Gunakan algoritma 
# BFS untuk menampilkan urutan kunjungan node dimulai dari Rumah. 

# Import deque dari collections untuk membuat queue (antrian)
from collections import deque 

# Fungsi BFS untuk menelusuri graph
def bfs(graph, start): 
    visited = set()         # Set untuk menyimpan node yang sudah dikunjungi
    queue = deque([start])  # Queue berisi node awal (start)

    visited.add(start)       # Tandai node awal sebagai sudah dikunjungi

    # Selama queue tidak kosong, lakukan perulangan
    while queue: 
        node = queue.popleft()  # Ambil node paling depan dari queue
        print(node, end=" ")    # Cetak node yang sedang dikunjungi

        # Periksa semua tetangga dari node
        for neighbor in graph[node]: 
            if neighbor not in visited:     # Jika tetangga belum dikunjungi
                visited.add(neighbor)       # Tandai sebagai sudah dikunjungi
                queue.append(neighbor)      # Masukkan ke queue untuk dikunjungi nanti

# Panggil fungsi BFS mulai dari node 'Rumah'
print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 

'''
Pertanyaan Analisis 
1. Node mana yang dikunjungi pertama?  
2. Mengapa BFS cocok untuk mencari jalur terdekat?  
3. Apa perbedaan urutan BFS jika struktur graph diubah? 

Jawaban:
1. Node pertama yang dikunjungi adalah "Rumah", karena BFS selalu mulai dari titik awal (start node) 
yang kita tentukan. Di program. start-nya 'Rumah'.

2. Karena BFS bekerja dengan cara menjelajah level demi level. Artinya, dia akan cek semua tetangga 
(node yang langsung terhubung) dulu sebelum lanjut ke node yang lebih jauh. Jadi kalau ada jalur terdekat, 
BFS pasti ketemu duluan sebelum jalur yang lebih panjang.
Contoh: dari "Rumah" ke "Sekolah" langsung ketemu, dibanding harus lewat "Rumah → Toko → Pasar → …". 
BFS akan pilih yang paling dekat dulu.

3. Urutan kunjungan node akan berubah sesuai hubungan antar node. Kalau isi dictionary graph diubah, 
misalnya "Rumah" terhubung ke "Pasar" dulu baru ke "Sekolah", maka urutan BFS juga akan berubah.
'''