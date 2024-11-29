from bangun_datar import hitung_luas_lingkaran, hitung_luas_persegi, hitung_luas_persegi_panjang, hitung_luas_segitiga, hitung_luas_trapesium
from bangun_ruang import hitung_luas_kubus, hitung_luas_balok

def hitung_bangun_datar():
    print("Pilih Bangun Datar:")
    print("1. Persegi")
    print("2. Segitiga")
    print("3. Lingkaran")
    print("4. Persegi Panjang")
    print("5. Trapesium")
    pilihan = int(input("Masukkan pilihan (1/5): "))

    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        print(f"Luas Persegi: {hitung_luas_persegi(sisi)}")
    elif pilihan == 2:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        print(f"Luas Segitiga: {hitung_luas_segitiga(alas, tinggi)}")
    elif pilihan == 3:
        jarijari = float(input("Masukkan jari-jari: "))
        print(f"Luas Lingkaran: {hitung_luas_lingkaran(jarijari)}")
    elif pilihan == 4:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        print(f"Luas Persegi Panjang: {hitung_luas_persegi_panjang(panjang, lebar)}")
    elif pilihan == 5:
        sisi_atas = float(input("Masukkan sisi atas: "))
        sisi_bawah = float(input("Masukkan sisi bawah: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Luas Trapesium: {hitung_luas_trapesium(sisi_atas, sisi_bawah, tinggi)}")
    else:
        print("Pilihan tidak valid!")

def hitung_bangun_ruang():
    print("Pilih bangun ruang:")
    print("1. Kubus")
    print("2. Balok")
    pilihan = int(input("Masukkan pilihan (1/2): "))

    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi kubus: "))
        print(f"Luas kubus: {hitung_luas_kubus(sisi)}")
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        print(f"Luas balok: {hitung_luas_balok(panjang, lebar, tinggi)}")
    else:
        print("Pilihan tidak valid!")
