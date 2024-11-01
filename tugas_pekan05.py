kendaraan = ['beat karbu', 'sepeda ontel', 200, 'pink', 2]

kendaraan.append('13jt')
kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))


print()
print("""Pilih salah satu:
1. Hitung Luas Persegi
2. Hitung Luas Lingkaran                    
3. Hitung Luas Segitiga
""")
hitung_luas = input('pilih antara 1 - 3 :')
match hitung_luas:
    case '1':
        print('Menghitung Luas Persegi')
        sisi = int(input('Masukan Nilai Sisi: '))
        hitung_luas_persegi = sisi * sisi
        print(f'jadi luas persegi dengan sisi {sisi} cm, adalah {hitung_luas_persegi} cm^2')
    case '2':
        print('Menghitung Luas Lingkaran')
        jari = int(input('Masukan Nilai Jari-jari: '))
        hitung_luas_lingkaran = 3.14 * jari**2
        print(f'jadi luas Lingkaran dengan Jari-jari {jari} cm, adalah {hitung_luas_lingkaran} cm^2')
    case '3':
        print('Menghitung Luas Segitiga')
        a = int(input('Masukan Nilai Alas: '))
        t = int(input('Masukan Nilai Tinggi: '))
        hitung_luas_segitiga = 1/2 * a * t
        print(f'jadi luas Segitiga dengan Alas {a} cm, dan Tinggi {t} adalah {hitung_luas_segitiga} cm^2')
    case _:
        print('pilihan tidak valid')
