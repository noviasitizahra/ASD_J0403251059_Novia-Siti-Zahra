# =====================================================
# PRAKTIKUM 1 : KONSEP ADT DAN FILE HANDLING
# Latihan Dasar 1 : MEMBACA SELURUH ISI FILE
# =====================================================

# MEMBUKA FILE DENGAN MODE READ ("r")

# MEMBUKA FILE DALAM SATU STRING
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    isi_file = file.read() #MEMBACA KESELUURUHAN ISI FILE DALAM SATU STRING
print(isi_file)

# parameter r

print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)

# MEMBUKA FILE PER BARIS
print("===Membaca File per BARIS===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris +1
        baris = baris.strip() #MENGHILANGKAN BARIS BARU
        print("Baris ke-", jumlah_baris)
        print("Isinya", baris)

print("")
# =====================================================
# PRAKTIKUM 1 : KONSEP ADT DAN FILE HANDLING
# Latihan Dasar 2 : Parsing baris menjadi kolom data
# =====================================================
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") # MENSPLIT/MEMISAHKAN SATU DATA DENGAN YANG LAIN
        print("NIM:", nim, "| Nama:", nama, "| Nilai:", nilai)

print("")
# =====================================================
# PRAKTIKUM 1 : KONSEP ADT DAN FILE HANDLING
# Latihan Dasar 3 : MEMBACA FILE DAN MENYIMPAN KE LIST
# =====================================================

data_list = [] #List untuk menampung data mahasiswa
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        # SIMPAN SEBAGAI LIST "[NIM, NAMA, NILAI]"
        data_list.append([nim,nama,int(nilai)])

print("=====DATA MAHASISWA DALAM LIST=====")
print(data_list)

print("=====JUMLAH RECORD DALAM LIST=====")
print("Jumlah Record", len(data_list))

print("MENAMPILKAN DATA RECORD TERTENTU")
print("CONTOH RECORD PERTAMA: ", data_list[0]) #ARRAY DIMULAI DARI 0

print("")
# =====================================================
# PRAKTIKUM 1 : KONSEP ADT DAN FILE HANDLING
# Latihan Dasar 4 : MEMBACA FILE DAN MENYIMPAN KE DICTIONARY
# =====================================================

data_dict = {} # Buat variabel untuk dictionary
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        # simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim] = {      # KEY
            "nama": nama,       # VALUES
            "nilai": int(nilai) #VALUES
        }
print("=====DATA MAHASISWA DALAM DICTIONARY=====")
print(data_dict)

