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
            preorder(node.left)
            preorder(node.right)

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

# menjalankan traversal preorder
print("Hasil traversal preorder: ")
preorder(root)

# penjelasan
'''
Traversal preorder adalah cara membaca isi pohon biner dengan urutan tertentu, yaitu dimulai dari root terlebih dahulu, kemudian anak kiri, dan terakhir anak kanan.
Jadi setiap kali kita berada di sebuah node, hal pertama yang dilakukan adalah mencetak data node tersebut.
Setelah itu, kita masuk ke cabang kiri dan melakukan hal yang sama secara rekursif, lalu berlanjut ke cabang kanan. 
Dengan pola ini, seluruh isi pohon akan terbaca dari atas ke bawah sesuai urutan root–left–right.

Sebagai contoh, jika kita punya pohon dengan root A, anak kiri B, anak kanan C, lalu B punya anak D dan E, serta C punya anak F dan G, maka hasil traversal preorder akan menjadi A B D E C F G. 
Urutan ini muncul karena kita selalu mendahulukan root, lalu menelusuri semua cabang kiri sampai habis, baru kemudian pindah ke cabang kanan.
Konsep rekursif di dalam fungsi preorder membuat proses ini berjalan otomatis tanpa harus menuliskan perintah cetak untuk setiap node satu per satu.
Dengan begitu, traversal preorder memudahkan kita membaca struktur pohon secara sistematis dan konsisten.

'''