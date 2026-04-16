# ============================================
# Nama  : Novia Siti Zahra
# Kelas : B1
# NIM   : J0403251059
# Latihan 6 : 
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

# penjelasan
'''
Traversal preorder adalah cara membaca pohon dengan urutan root → anak kiri → anak kanan.
Dalam contoh struktur organisasi, root adalah Direktur, lalu kita menelusuri anak kiri yaitu Manajer A beserta staf-stafnya, kemudian beralih ke anak kanan yaitu Manajer B dan stafnya.
Hasil traversal preorder dari pohon ini adalah Direktur Manajer A Staff 1 Staff 2 Manajer B Staff 3. 
Urutan ini mencerminkan bagaimana kita membaca organisasi dari pucuk pimpinan, lalu ke bagian kiri terlebih dahulu, dan akhirnya ke bagian kanan.
Dengan pola ini, kita bisa melihat struktur organisasi secara sistematis mulai dari atas hingga ke bawah sesuai cabang yang ada.
'''