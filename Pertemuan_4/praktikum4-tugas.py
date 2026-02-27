# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ========================================================== 
# Tugas Hands-On: Sistem Antrian Bengkel Motor 
# ========================================================== 
 
# =========================
# class node
# =========================
# node digunakan untuk menyimpan data pelanggan
# setiap node memiliki:
# no      : nomor antrian
# nama    : nama pelanggan
# servis  : jenis servis
# next    : pointer ke node berikutnya
class Node: 
    def __init__(self, no, nama, servis): 
        self.no = no 
        self.nama = nama 
        self.servis = servis 
        self.next = None    # pointer ke node selanjutnya
 
# =========================
# class QueueBengkel
# =========================
# Queue menggunakan prinsip FIFO (First In First Out)
# Menggunakan Linked List dengan dua pointer:
# front : menunjuk ke pelanggan terdepan
# rear  : menunjuk ke pelanggan terakhir
class QueueBengkel: 
    def __init__(self): 
        self.front = None   # awal antrian
        self.rear = None    # akhir antrian 
 
    # =========================
    # method enqueue
    # =========================
    # menambahkan pelanggan ke belakang antrian
    def enqueue(self, no, nama, servis): 
        # membuat node baru
        node_baru = Node(no, nama, servis)

        # jika antrian kosong
        if self.front is None:
            # front dan rear sama-sama menunjuk ke node baru
            self.front = node_baru
            self.rear = node_baru
        else:
            # node terakhir (rear) menunjuk ke node baru
            self.rear.next = node_baru
            # geser rear ke node baru
            self.rear = node_baru

        print("Pelanggan berhasil ditambahkan ke antrian!")
 
    # =========================
    # method dequeue
    # =========================
    # menghapus pelanggan terdepan
    def dequeue(self): 
        # jika antrian kosong
        if self.front is None:
            print("Antrian kosong. Tidak ada pelanggan untuk dilayani")
            return

        # simpan data pelanggan terdepan
        dilayani = self.front

        # geser front ke node berikutnya
        self.front = self.front.next

        # jika setelah dihapus antrian menjadi kosong
        if self.front is None:
            self.rear = None  # rear juga harus dikosongkan

        print("\nPelanggan sedang dilayani:")
        print("No Antrian :", dilayani.no)
        print("Nama       :", dilayani.nama)
        print("Servis     :", dilayani.servis)
 
    # =========================
    # method tampilkan
    # =========================
    # menampilkan seluruh isi antrian
    def tampilkan(self): 
        # jika antrian kosong
        if self.front is None:
            print("Antrian kosong.")
            return

        print("\n===== DAFTAR ANTRIAN =====")

        # pointer sementara untuk traversal
        current = self.front

        # traversal dari front sampai None
        while current is not None:
            print("---------------------------")
            print("No Antrian :", current.no)
            print("Nama       :", current.nama)
            print("Servis     :", current.servis)
            current = current.next  # pindah ke node berikutnya

        print("---------------------------") 

# =========================
# fungsi main (menu program)
# =========================
def main(): 
    # membuat objek QueueBengkel
    q = QueueBengkel() 
 
    # perulangan menu utama
    while True: 
        print("\n=== Sistem Antrian Bengkel ===") 
        print("1. Tambah Pelanggan") 
        print("2. Layani Pelanggan") 
        print("3. Lihat Antrian") 
        print("4. Keluar") 
 
        pilih = input("Pilih menu: ") 
 
        # menu Tambah Pelanggan
        if pilih == "1": 
            no = input("No Antrian : ") 
            nama = input("Nama      : ") 
            servis = input("Servis    : ") 
            q.enqueue(no, nama, servis) 
 
        # menu Layani Pelanggan
        elif pilih == "2": 
            q.dequeue() 
 
        # menu Lihat Antrian
        elif pilih == "3": 
            q.tampilkan() 
 
        # menu Keluar
        elif pilih == "4": 
            break 
 
        # jika input tidak valid
        else: 
            print("Pilihan tidak valid") 
 
# menjalankan program
if __name__ == "__main__": 
    main()