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
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ") # root

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
'''
Traversal postorder adalah cara membaca pohon biner dengan urutan anak kiri → anak kanan → root.
Artinya, setiap kali kita berada di sebuah node, kita harus masuk dulu ke cabang kiri sampai habis, lalu lanjut ke cabang kanan, dan setelah itu baru mencetak data dari node sekarang. 
Dengan pola ini, root akan selalu dicetak paling akhir setelah semua anak-anaknya selesai dibaca.
Sebagai contoh, jika kita punya pohon dengan root A, anak kiri B, anak kanan C, lalu B punya anak D dan E, serta C punya anak F dan G, maka hasil traversal postorder adalah D E B F G C A.
Urutan ini muncul karena kita selalu mendahulukan cabang kiri, kemudian cabang kanan, dan terakhir root. 
Traversal postorder sering digunakan ketika kita ingin menghapus atau memproses pohon dari bawah ke atas, karena setiap node baru diproses setelah semua anak-anaknya selesai.
Dengan begitu, traversal postorder memberikan cara sistematis untuk membaca pohon dari bagian paling bawah hingga ke puncak.
'''