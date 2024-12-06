class Gempa:
    #Konstruktor inisialisasi atribut lokasi dan skala
    #Method adalah fungsi yang berada di dalam class
    def __init__(self, lokasi, skala):
        
        #atribut
        self.lokasi = lokasi
        self.skala = skala 

    #Method  menentukan dampak skala gempa
    def dampak(self):
        
        #statement / logika
        if self.skala < 2:
            print('Dampak gempa tidak berasa')
        elif self.skala >= 2 and self.skala <= 4:
            print("Dampak gempa bangunan retak-retak")
        elif self.skala > 4 and self.skala <= 6:
            print("Dampak gempa bangunan roboh")
        elif self.skala > 6:
            print("Dampak gempa bangunan roboh dan berpotensi Tsunami")

        #menampilkan lokasi dan skala
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')