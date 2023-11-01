def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

def hitung_luas_lingkaran(jari_jari):
    import math
    luas = math.pi * (jari_jari ** 2)
    return luas

pilihan = input("Pilih bangun datar (1,2,3): ").lower()

if pilihan == "1":
    sisi = float(input("Masukkan panjang sisi: "))
    luas = hitung_luas_persegi(sisi)
    print(f"Luas persegi adalah: {luas}")

elif pilihan == "2":
    alas = float(input("alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = hitung_luas_segitiga(alas, tinggi)
    print(f"Luas segitiga adalah: {luas}")

elif pilihan == "3":
    jari_jari = float(input("Masukkan panjang jari-jari: "))
    luas = hitung_luas_lingkaran(jari_jari)
    print(f"Luas lingkaran adalah: {luas}")

else:
    print("Pilihan tidak valid. Silakan pilih bangun datar yang benar.")




# Membuat variabel list dengan informasi kendaraan
kendaraan = [
    ["Mobil", "Sedan", "1800cc", "Merah", 4],
    ["Sepeda Motor", "Bebek", "150cc", "Hitam", 2],
    ["Sepeda", "Gunung", "N/A", "Hijau", 2]
] 

# Menambahkan harga kendaraan ke dalam list
harga_kendaraan = [25000, 8000, 500]

# Menambahkan merk kendaraan ke dalam list
merk_kendaraan = ["Toyota", "Honda", "Trek"]

# Menambahkan harga dan merk ke dalam list kendaraan
for i in range(len(kendaraan)):
    kendaraan[i].append(harga_kendaraan[i])
    kendaraan[i].insert(1, merk_kendaraan[i])

# Menampilkan list kendaraan setelah ditambahkan harga dan merk
for data_kendaraan in kendaraan:
    print(data_kendaraan)