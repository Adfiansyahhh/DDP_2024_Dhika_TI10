from animal import animal

class kelinci(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.warna = warna

    def info_kelinci(self):
        super().info_animal()
        print("Habitat\t\t\t: ", self.habitat,
            "\nWarna\t\t\t: ", self.warna)
        
print()
kelinci = kelinci('Kelinci', 'Wortel', '10 Tahun', 'Melahirkan', 'Dipelihara', 'Warna')
print('## Info Kelinci')
kelinci.info_kelinci()