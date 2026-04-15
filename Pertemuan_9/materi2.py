# ============================================
# Nama  : Novia Siti Zahra
# Kelas : B1
# NIM   : J0403251059
# Latihan 2 : membuat binary tree sederhana
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
        print("Child kiri root", root.left.data)
        print("Child kanan root", root.right.data)
        print("Child kiri dari B: ", root.left.left.data)
        print("Child kanan dari B: ", root.left.right.data)
# lanjutkan keseluruhan tree
# penjelasan 