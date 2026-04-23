#============================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ===========================================

#======================================================
# Latihan 1 : node dan insert binary search tree (BST)
# =====================================================

# Class Node digunakan untuk membuat 1 simpul (node) di BST
class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai data
        self.left = None    # pointer ke anak kiri
        self.right = None   # pointer ke anak kanan

# Fungsi insert untuk menambahkan data ke dalam BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    
    # Jika data lebih kecil dari root, masuk ke kiri
    if data < root.data:
        root.left = insert(root.left, data)

    # Jika data lebih besar dari root, masuk ke kanan
    elif data > root.data:
        root.right = insert(root.right, data)

     # Kembalikan root (biar struktur pohon tetap tersambung)
    return root

# mengisi data BST
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]

# Loop untuk memasukkan semua data ke BST satu per satu
for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat")

#============================================
# Latihan 2 : traversal inorder
# ===========================================

# Fungsi inorder untuk menampilkan isi BST secara urut (kecil -> besar)
def inorder(root):
    # Jika node tidak kosong
    if root is not None:
        inorder(root.left)          # kunjungi subtree kiri dulu
        print(root.data, end=" ")   # tampilkan data root
        inorder(root.right)         # lalu kunjungi subtree kanan

print("Hasil Inorder: ")
inorder(root)   # menampilkan semua data BST

#============================================
# Latihan 3 : search di BST
# ===========================================

# Fungsi search untuk mencari data dalam BST
def search(root, key):
    # Jika root kosong, data tidak ditemukan
    if root is None:
        return False
    
    # Jika data ditemukan
    if root.data == key:
        return True
    
    # Jika key lebih kecil, cari ke kiri
    elif key < root.data:
        return search(root.left, key)
    
    # Jika key lebih besar, cari ke kanan
    else:
        return search(root.right, key)
    
# uji pencarian
key = 100

# Mengecek apakah data ada atau tidak
if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")