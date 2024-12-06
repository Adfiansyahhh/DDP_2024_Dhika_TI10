# Memanggil file gempa dan import semua method/fungsi
from Gempa import *

#membuat object gempa dengan argumen 
gempa1 = Gempa('banten', 1.2)
gempa2 = Gempa('palu', 6.1)
gempa3 = Gempa('cianjur', 5.6)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.0)

# Informasi gempa
print("## Info Gempa Maseh ##")
print()
gempa1.dampak()

print("## Info Gempa Maseh ##")
print()
gempa2.dampak()

print("## Info Gempa Maseh ##")
print()
gempa3.dampak()

print("## Info Gempa Maseh ##")
print()
gempa4.dampak()

print("## Info Gempa Maseh ##")
print()
gempa5.dampak()