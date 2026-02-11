# ====== NODE DOUBLY ======
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# ====== DOUBLY LINKED LIST ======
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # ====== LATIHAN 3: SEARCH ======
    def search(self, key):
        if not self.head:
            print("Doubly Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
                return
            temp = temp.next

        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")


# ====== TAMPILAN ======
dll = DoublyLinkedList()
dll.insert_at_end(2)
dll.insert_at_end(6)
dll.insert_at_end(9)
dll.insert_at_end(14)
dll.insert_at_end(20)

dll.search(9)
dll.search(10)
