from animal import animal

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, bernafas):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.bernafas = bernafas

    def info_ikan(self):
        super().info_animal()
        print("Warna\t\t\t: ", self.habitat,
            "\nBernafas Dengan\t\t: ", self.bernafas)
        
print()
ikan = ikan('Hiu', 'Ikan', '10 Tahun', 'Melahirkan', 'Insang', 'Laut')
print('## Info Ikan ##')
ikan.info_ikan()