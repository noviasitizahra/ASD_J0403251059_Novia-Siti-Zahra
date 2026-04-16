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
        print(node.data, end="")
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
        root.right.left = Node("F")
        root.right.right = Node("G")

        print("Hasil traversal inorder: ")
        inorder(root)

        # penjelasan
        '''
        Traversal inorder adalah cara membaca pohon biner dengan urutan anak kiri → root → anak kanan.
        Artinya, setiap kali kita berada di sebuah node, kita harus masuk dulu ke cabang kiri sampai habis, lalu kembali ke node sekarang untuk mencetak datanya, dan terakhir masuk ke cabang kanan. Dengan pola ini, data pohon akan terbaca dari kiri ke kanan secara berurutan.
        Sebagai contoh, jika kita punya pohon dengan root A, anak kiri B, anak kanan C, lalu B punya anak D dan E, serta C punya anak F dan G, maka hasil traversal inorder adalah D B E A F C G. 
        Urutan ini muncul karena kita selalu mendahulukan cabang kiri, kemudian root, lalu cabang kanan.
        Traversal inorder sering dipakai karena hasilnya terlihat seperti urutan data yang rapi dari kiri ke kanan, mirip membaca teks dari awal sampai akhir.
        '''