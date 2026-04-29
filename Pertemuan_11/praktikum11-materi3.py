# ==================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==================================

# ========================================
# Implementasi Depth-First Search (DFS) 
# ========================================

# Representasi graph menggunakan adjacency list
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

def dfs(graph, node, visited): 
    """ 
    Fungsi untuk melakukan penelusuran graph menggunakan DFS. 
    Parameter: 
    graph   : dictionary yang menyimpan struktur graph 
    node   
    : node yang sedang dikunjungi 
    visited : set untuk menyimpan node yang sudah dikunjungi 
    """ 
    # Tandai node saat ini sebagai sudah dikunjungi 
    visited.add(node) 
    
    # Tampilkan node yang sedang dikunjungi 
    print(node, end=" ") 

    # Periksa semua tetangga dari node saat ini 
    for neighbor in graph[node]: 

        # Jika tetangga belum pernah dikunjungi 
        if neighbor not in visited: 

            # Lakukan DFS secara rekursif ke tetangga tersebut 
            dfs(graph, neighbor, visited) 

# Set kosong untuk menyimpan node yang sudah dikunjungi 
visited = set() 

# Menjalankan DFS mulai dari node A 
print("Urutan DFS:") 
dfs(graph, 'A', visited)