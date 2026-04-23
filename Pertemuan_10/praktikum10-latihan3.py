#============================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ===========================================

#=================================================
# Latihan 5 : rotasi kiri pada BST tidak seimbang
# ================================================

# Class Node untuk membuat node pada tree
class Node: 
    def __init__(self, data): 
        self.data = data    # menyimpan nilai pada node
        self.left = None    # child kiri (lebih kecil dari data)
        self.right = None   # child kanan (lebih besar dari data)
 
 
# Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ")   # tampilkan root dulu
        preorder(root.left)         # lalu ke kiri
        preorder(root.right)        # lalu ke kanan
 
 
# Fungsi untuk menampilkan struktur tree (biar keliatan bentuknya)
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R") 

# Fungsi rotasi kiri 
def rotate_left(x): 
    # x adalah root lama 
    y = x.right       # y adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara 
 
    # Proses rotasi 
    y.left = x        # x menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2 
 
    # y menjadi root baru 
    return y 

# ----------------------------- 
# Program utama 
# ----------------------------- 

# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
root = Node(10) 
root.right = Node(20) 
root.right.right = Node(30) 

print("Preorder sebelum rotasi kiri:") 
preorder(root)  # lihat isi tree sebelum rotasi

print("\n\nStruktur sebelum rotasi kiri:") 
tampil_struktur(root)   # lihat bentuk tree sebelum rotasi

# Melakukan rotasi kiri pada root 
root = rotate_left(root) 

print("\nPreorder sesudah rotasi kiri:") 
preorder(root)  # lihat isi tree setelah rotasi

print("\n\nStruktur sesudah rotasi kiri:") 
tampil_struktur(root)       # lihat bentuk tree setelah rotasi 