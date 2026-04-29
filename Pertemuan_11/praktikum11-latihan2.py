# ==================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==================================

# ====================================================
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur) 
# ====================================================

# Graph berikut merepresentasikan jalur eksplorasi: 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 

# Gunakan algoritma DFS untuk menelusuri graph mulai dari node A. 
def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 

    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited)

visited = set() 

print("DFS dari A:") 
dfs(graph, 'A', visited) 

'''
Pertanyaan Analisis 
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
2. Apa yang terjadi jika urutan neighbor diubah?  
3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 


'''