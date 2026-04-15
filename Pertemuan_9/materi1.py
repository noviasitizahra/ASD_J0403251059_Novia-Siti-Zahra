# ============================================
# Nama  : Novia Siti Zahra
# Kelas : B1
# NIM   : J0403251059
# Latihan 1 : membuat node
# ============================================


# class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan

        # membuat root
        root = Node("A")
        
        # menampilkan isi node
        print("Data pada root", root.data)
        print("Data child kiri root", root.left)
        print("Data child kanan root", root.right)