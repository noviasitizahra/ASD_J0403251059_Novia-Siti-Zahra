# ==================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==================================

# ====================================================
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur) 
# ====================================================

# Graph berikut merepresentasikan jalur eksplorasi dalam bentuk dictionary: 
# Key = node, Value = daftar node tetangga yang terhubung
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 

# Gunakan algoritma DFS untuk menelusuri graph mulai dari node A. 
# Fungsi DFS untuk menelusuri graph
def dfs(graph, node, visited): 
    visited.add(node)       # Tandai node sebagai sudah dikunjungi
    print(node, end=" ")    # Cetak node yang sedang dikunjungi

    # Telusuri semua tetangga dari node
    for neighbor in graph[node]: 
        if neighbor not in visited:         # Jika tetangga belum dikunjungi
            dfs(graph, neighbor, visited)   # Rekursif masuk ke tetangga

# Set untuk menyimpan node yang sudah dikunjungi
visited = set() 

# Panggil fungsi DFS mulai dari node 'A'    
print("DFS dari A:") 
dfs(graph, 'A', visited) 

'''
Pertanyaan Analisis 
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
2. Apa yang terjadi jika urutan neighbor diubah?  
3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 

Jawaban:
1. Karena DFS menggunakan rekursi (atau stack) yang selalu masuk ke cabang berikutnya sampai habis,
    baru kembali ke atas. Jadi jalur terdalam dieksplorasi dulu.

2. Urutan kunjungan node juga ikut berubah. DFS akan mengikuti urutan tetangga yang ada di list graph.
      Misalnya kalau 'A' punya ['C','B'] bukan ['B','C'], maka DFS akan masuk ke 'C' dulu.

3. DFS: fokus ke jalur dalam dulu (contoh hasil: A B D E C F).
    BFS: fokus ke level demi level (contoh hasil: A B C D E F).
    Jadi urutan kunjungan berbeda karena cara kerja algoritmanya berbeda.
'''