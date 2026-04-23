#============================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ===========================================

#======================================================
# Latihan 1 : node dan insert binary search tree (BST)
# =====================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# alur fungsi insert ------
def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

# mengisi data BST
root = None
data_list = [50, 38, 78, 20, 40, 60, 88]

for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat")

#============================================
# Latihan 2 : traversal inorder
# ===========================================

# alur fungsi inorder------
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
print("Hasil Inorder: ")
inorder(root)

#============================================
# Latihan 3 : search di BST
# ===========================================

def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    elif key < root.data:
        return search(root.left, key)
    
    else:
        return search(root.right, key)
    
# uji pencarian
key = 100

if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")