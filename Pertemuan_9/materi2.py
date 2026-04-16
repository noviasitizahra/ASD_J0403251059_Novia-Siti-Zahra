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
        root.right.left = Node("F")
        root.right.right = Node("G")
        
        # menampilkan isi node
        print("Data pada root: ", root.data)
        print("Child kiri root: ", root.left.data)
        print("Child kanan root: ", root.right.data)
        print("Child kiri dari B: ", root.left.left.data)
        print("Child kanan dari B: ", root.left.right.data)
        print("Child kiri dari C: ", root.right.left.data)
        print("Child kanan dari C: ", root.right.right.data)

# penjelasan 
# 1. Node itu ibarat titik atau simpul dalam pohon. Setiap node bisa punya anak kiri (left) dan anak kanan (right)
# 2. Root adalah node paling atas, pusat dari pohon. Di sini root kita adalah A.
# 3. Dari root, kita bisa bikin cabang ke kiri (B) dan ke kanan (C).
# 4. Lalu dari B, kita bikin anak lagi yaitu D (kiri) dan E (kanan).
# 5. Dari C, kita juga bikin anak yaitu F (kiri) dan G (kanan).