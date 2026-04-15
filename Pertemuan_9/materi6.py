# ============================================
# Nama  : Novia Siti Zahra
# Kelas : B1
# NIM   : J0403251059
# Latihan 6 : membuat binary search
# ============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        print(node.left)
        print(node.right)
        
# membuat tree struktur organisasi
root = Node("Direktur")

# child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

# menjalankan traversal preorder
print("Struktur organisasi (preorder): ")
preorder(root)