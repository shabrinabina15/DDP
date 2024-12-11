from Animal import *
print("======================Hewan Ular========================")
class Ular(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_biak, Design, Racun):
        super().__init__(Nama, Makanan, Hidup, Berkembang_biak)
        self.Design = Design
        self.Racun = Racun
        
    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t\t: ", self.Design,
              "\nRacun \t\t\t\t: ", self.Racun)
        
Sawah = Ular("Sawah/Welang-weling", "Ayam", "Persawahan", "Bertelur", "Loreng-loreng", "Tidak Berbisa")
Sawah.cetak_ular()