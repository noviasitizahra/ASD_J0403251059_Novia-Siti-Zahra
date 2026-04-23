#============================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ===========================================

#=================================================
# Latihan 6 : rotasi kanan pada BST tidak seimbang
# ================================================

# Class Node untuk membuat node pada tree
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai pada node
        self.left = None      # menunjuk ke anak kiri (lebih kecil)
        self.right = None     # menunjuk ke anak kanan (lebih besar)


# Fungsi preorder untuk melihat isi tree
# Urutan: root -> kiri -> kanan
def preorder(root):
    if root is not None:
        print(root.data, end=" ")   # tampilkan root dulu
        preorder(root.left)        # lalu ke subtree kiri
        preorder(root.right)       # lalu ke subtree kanan


# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        # "   " * level digunakan untuk memberi jarak (indentasi)
        print("   " * level + f"{posisi}: {root.data}")

        # tampilkan anak kiri
        tampil_struktur(root.left, level + 1, "L")

        # tampilkan anak kanan
        tampil_struktur(root.right, level + 1, "R")


# Fungsi rotasi kanan
def rotate_right(x):
    # x = root lama 
    y = x.left        # ambil anak kiri (ini nanti jadi root baru)
    T2 = y.right      # simpan subtree kanan milik y

    # Proses rotasi
    y.right = x       # x jadi anak kanan dari y
    x.left = T2       # anak kiri x diganti dengan T2

    # y jadi root baru
    return y


# -----------------------------
# Program utama
# -----------------------------

# Membuat tree tidak seimbang (condong ke kiri)
# karena data dimasukkan: 30, 20, 10
# sehingga bentuknya jadi seperti linked list ke kiri
# bentuk awal:
#     30
#    /
#   20
#  /
# 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)      # output: 30 20 10

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)


# Melakukan rotasi kanan pada root (30)
# tujuannya untuk menyeimbangkan tree
root = rotate_right(root)


print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)