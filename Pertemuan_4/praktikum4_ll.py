# ==================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : TPL B1
# ==================================================

# ==================================================
# Implementasi Dasar : Node pada Linked List
# ==================================================

class Node:
    def __init__(self,data): # konstruktor
        self.data = data # menyimpan nilai/data
        self.next = None # pointer ke note berikutnya (awal = none)

# 1) membuat Node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) menentukan node pertama (head)
head = nodeA

# 4) traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data) # menampilkan data pada node saat ini
    current = current.next # pindah ke node berikutnya


# ==================================================
# Implementasi Dasar : Linked List + Insert Awal
# ==================================================

class LinkedList: # class implementasi Stuck
    def __init__(self):
        self.head = None # awalnya kosong

    def insert_awal(self,data): # konsep push dalam stack
        # 1) buat node baru
        nodeBaru = Node(data) # panggil class node

        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # 3) head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self): # konsep pop dalam stack
        data_terhapus = self.head.data # konsep peek dalam stack
        # menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah : ", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("=== list baru ===")
ll = LinkedList() # instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
