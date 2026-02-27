# ================================================
# Nama  : Novia Siti Zahra
# NIM   : J0403251059
# Kelas : B1
# ================================================

# ================================================
# Studi kasus: sistem antrian layanan akademik
# Implementasi Queue => 
# Enqueue : memindahkan pointer rear (tambah data baru dari belakang)
# Dequeue : memindahkan pointer front (head) (menghapus data dari depan)
# Stack => Front -> C -> B-> A -> None
# Front -> A -> B -> C ->Rear
# ================================================

# 1) Mendefinisikan Node (unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim # menyimpan NIM mahasiswa
        self.nama = nama # menyimpan Nama mahasiswa
        self.next = None # pointer ke node berikutnya

# 2) Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # ketika queue kosong maka front = rear = none
        return self.front is None
    
    # menambahkan data baru ke bagian belakang (rear) => menambahkan antrian mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama) # instantiasi 
        # jika data baru masuk dari queue yg kosong maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # jika queue tidak kosong , maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada mahasiswa yang dilayani")
            return None
        # lihat data bagian front, simpan di variabel data yg akan dihapus (dilayani)
        node_dilayani = self.front

        # geser pointer front ke next front
        self.front = self.front.next
        # jika front menjadi none (data antrian terakhir yg dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):

        print("Daftar antrian mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

# PROGRAM UTAMA

def main():
    # instantiasi queue
    q = queueAkademik()

    while True:
        print("=== Sistem Antrian Akademik ===")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4) : ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()

            q.enqueue(nim,nama)
            print("Mahasiswa berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai... Terima kasih")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi 1-4")

# penanda eksekusi file utama
if __name__ == "__main__":
    main()