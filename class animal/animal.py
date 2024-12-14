class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print('Nama hewan\t\t: ', self.nama,
                "\nMakanan\t\t\t: ", self.makanan,
                "\nHidup\t\t\t: ", self.hidup,
                "\nBerkembang biak\t\t: ", self.berkembang_biak)
            
# kucing = animal('Kucing', 'Daging', 'Hidup', 'Melahirkan')

# kucing.info_animal()
        