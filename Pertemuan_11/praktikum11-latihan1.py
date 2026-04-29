# ==================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ==================================

# ====================================================
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
# ====================================================

graph = {
    'Rumah' : ['Sekolah', 'Toko'],
    'Sekolah' : ['Perpustakaan'],
    'Toko' : ['Pasar'],
    'Perpustakaan' : [],
    'Pasar' : []
}

from collections import deque 

def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 

    visited.add(start) 

    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 

        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 


print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 

'''
Pertanyaan Analisis 
1. Node mana yang dikunjungi pertama?  
2. Mengapa BFS cocok untuk mencari jalur terdekat?  
3. Apa perbedaan urutan BFS jika struktur graph diubah? 

Jawaban:
1. 
'''