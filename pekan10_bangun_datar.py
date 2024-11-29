import math

def hitung_luas_persegi(sisi):
    return sisi ** 2

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
 
def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def hitung_luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    return 0.5 * (sisi_atas + sisi_bawah) * tinggi
