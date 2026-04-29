# ==================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==================================

# ========================================
# implementasi Breadth-First Search (BFS) 
# ========================================

# struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

# representasi graph menggunakan adjacency list 
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'D'],
    'D' : ['B', 'C']
}

def bfs(graph, start):
    # fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimpan struktur graph
    # start : node awal penelusuran

    # set digunakan untuk menyimpan node yang sudah dikunjungi
    visited = set()

    # queue digunakan untuk menyimpan node yang akan diproses/dibaca
    queue = deque()

    # masukan node awal ke queue
    queue.append(start)

    # tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    print("Urutan BFS:")

    # selama queue tidak kosong, proses terus berjalan
    while queue:
        # ambil node paling depan dari queue
        node = queue.popleft()

        # tampilkan node yang sedang dikunjungi
        print(node, end=" ")

        # periksa semua tetangga dari node saat ini
        for neighbor in graph[node]:
            # jika tetangga belum pernah dikunjungi
            if neighbor not in visited:

                # tandai sebagai sudah dikunjungi
                visited.add(neighbor)

                # masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)
            
# menjalankan BFS dari node A
bfs(graph, 'A')


