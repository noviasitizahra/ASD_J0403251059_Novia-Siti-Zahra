# ============================================
# Nama  : Novia Siti Zahra
# Kelas : B1
# NIM   : J0403251059
# Latihan 3 : membuat traversal preorder
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

        # membuat root
        root = Node("A")

        # membuat child level 1
        root.left = Node("B")
        root.right = Node("C")

        # membuat child level 2
        root.left.left = Node("D")
        root.left.right = Node("E")

        # menjalankan traversal preorder
        print("Hasil traversal preorder: ")
        preorder(root)