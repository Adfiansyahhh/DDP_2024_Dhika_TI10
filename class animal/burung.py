from animal import animal

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    def info_burung(self):
        super().info_animal()
        print("Warna\t\t\t: ", self.warna,
              "\nParuh\t\t\t: ", self.paruh)
        

print()        
burung = burung("Puyuh", "Biji", "5 Tahun", "Menghasilkan Telur", "Coklat", "Lancip")
print('## Info Buyung ##')
burung.info_burung()