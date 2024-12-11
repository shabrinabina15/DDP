from Animal import *

print("======================Hewan Ikan========================")
class ikan(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_biak, Jenis, Motif):
        super().__init__(Nama, Makanan, Hidup, Berkembang_biak)
        self.Jenis = Jenis
        self.Motif = Motif
        
    def cetak_ikan(self):
        super().cetak()
        print("Jenis \t\t\t\t: ", self.Jenis,
              "\nMotif \t\t\t\t: ", self.Motif)
        
ikan = ikan("Koi", "Cacing", "Air Tawar", "Bertelur", "Asagi", "Oren Putih")
ikan.cetak_ikan()  