from Animal import *
print("=====================Hewan Kura - Kura=====================")
class Kurakura(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_biak, Jenis, Umur):
        super().__init__(Nama, Makanan, Hidup, Berkembang_biak)
        self.Jenis = Jenis
        self.Umur = Umur
        
    def cetak_Kurakura(self):
        super().cetak()
        print("Jenis \t\t\t\t: ", self.Jenis,
              "\nUmur \t\t\t\t: ", self.Umur)
        
Kurakura = Kurakura("Kura-Kura", "Sayuran", "Amphibi", "Bertelur", "Betina", "4 Tahun")
Kurakura.cetak_Kurakura()