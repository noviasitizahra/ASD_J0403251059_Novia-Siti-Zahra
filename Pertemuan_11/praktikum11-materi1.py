# ==================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==================================

# ========================================
# Konsep Dasar Graph  
# ========================================

graph = { 
    'A': ['B', 'C'], 
    'B': ['A', 'D'], 
    'C': ['A', 'D'], 
    'D': ['B', 'C'] 
} 

# ========================================
# mengakses Graph
# Untuk melihat isi graph, kita bisa menggunakan perulangan
# ========================================

# Mengambil setiap key dalam dictionary. Mengunjungi semua node satu per satu 
# Mengambil value dari key tersebut. Value ini adalah list tetangga (neighbors) 
# Menampilkan: node dan daftar tetangganya 
for node in graph:    
    print(node, "->", graph[node]) 