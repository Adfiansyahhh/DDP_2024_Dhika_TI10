from animal import animal

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, berbisa):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.berbisa = berbisa

    def info_ular(self):
        super().info_animal()
        print("Habitat\t\t\t: ", self.habitat,
            "\nBerbisa/Tidak Berbisa\t: ", self.berbisa)
        
print()
ular = ular('Cobra', 'Tikus/Hewan - hewan Kecil', '10 Tahun', 'Bertelur dan Melahirkan', 'Rawa', 'Berbisa')
print('## Info Ular ##')
ular.info_ular()