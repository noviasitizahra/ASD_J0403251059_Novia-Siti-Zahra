#============================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ===========================================

#============================================
# Latihan 4 : membuat BST yang tidak seimbang
# ===========================================

# Class Node untuk menyimpan data BST 
class Node: 
    def __init__(self, data): 
        self.data = data      # menyimpan nilai pada node (menyimpan nilai pada node)
        self.left = None      # child kiri (lebih kecil dari data)
        self.right = None     # child kanan (lebih besar dari data)

# Fungsi insert untuk menambahkan data ke BST  
def insert(root, data): 
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 

    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 
 
    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 
 
    return root  

# Fungsi preorder untuk melihat isi/bentuk tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        # "   " * level buat ngasih jarak biar keliatan bertingkat
        print("   " * level + f"{posisi}: {root.data}") 

        # tampilkan anak kiri (L)
        tampil_struktur(root.left, level + 1, "L") 

        # tampilkan anak kanan (R)
        tampil_struktur(root.right, level + 1, "R") 

# ----------------------------- 
# Program utama 
# ----------------------------- 
root = None     # awalnya tree kosong

# Data dimasukkan berurutan naik (ini yang bikin BST jadi tidak seimbang)
data_list = [10, 20, 30] 

# Memasukkan data satu per satu ke BST
for data in data_list: 
    root = insert(root, data) 

print("Preorder BST:") 
preorder(root)  # menampilkan isi tree dengan urutan preorder

print("\n\nStruktur BST:") 
tampil_struktur(root)   # menampilkan bentuk struktur tree