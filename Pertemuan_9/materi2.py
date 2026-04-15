# ============================================
# Nama  : Novia Siti Zahra
# Kelas : B1
# NIM   : J0403251059
# Latihan 2 : membuat binary search
# ============================================


# class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan

        # membuat root
        root = Node("A")

        # membuat child level 1
        root.left = Node("B")
        root.right = Node("C")

        # membuat child level 2
        root.left.left = Node("D")
        root.left.right = Node("E")
        
        # menampilkan isi node
        print("Data pada root", root.data)
        print("Data child kiri root", root.left.data)
        print("Data child kanan root", root.right.data)
        print("Child kiri dari B: ", root.left.left.data)
        print("Child kanan dari B: ", root.left.right.data)
# lanjutkan keseluruhan tree
# penjelasan 




# ============================================
# Nama  : Novia Siti Zahra
# Kelas : B1
# NIM   : J0403251059
# Latihan 4 : membuat traversal inorder
# ============================================

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan

# membuat fungsi inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        inorder(node.data, end="")
        inorder(node.right)

    # membuat tree
    # membuat root
        root = Node("A")

        # membuat child level 1
        root.left = Node("B")
        root.right = Node("C")

        # membuat child level 2
        root.left.left = Node("D")
        root.left.right = Node("E")

# ============================================
# Nama  : Novia Siti Zahra
# Kelas : B1
# NIM   : J0403251059
# Latihan 5 : membuat traversal postorder
# ============================================


# class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan

# membuat traversal postorder: left -> right -> root
def postorder(node):
    if node is not None:
        print(node.data, end=" ") # root
        postorder(node.left)
        postorder(node.right)

        # membuat tree
        # membuat root
        root = Node("A")

        # membuat child level 1
        root.left = Node("B")
        root.right = Node("C")

        # membuat child level 2
        root.left.left = Node("D")
        root.left.right = Node("E")
        
        # menjalankan traversal postorder
        print("Hasil traversal postorder: ")
        postorder(root)

        # penjelasan