from hitung import hitung_bangun_datar, hitung_bangun_ruang

def main():
    print("Pilih jenis perhitungan:")
    print("1. Luas Bangun Datar")
    print("2. Luas Bangun Ruang")
    pilihan = int(input("Masukkan pilihan (1/2): "))

    if pilihan == 1:
        hitung_bangun_datar()
    elif pilihan == 2:
        hitung_bangun_ruang()
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
