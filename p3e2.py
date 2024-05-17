class Mahasiswa:
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.nama = "Agfan Herru Pratama Hendarsin"
        self.nim = "064002100043"
        self.fakultas = "Teknik Industri"
        self.hobi = "Melamun di WC"

    def hitung_luas_persegi_panjang(self):
        return self.panjang * self.lebar

    def info_persegi_panjang(self):
        return f"{self.nama} {self.nim} {self.fakultas}\n----->PROGRAM MENGHITUNG LUAS PERSEGI PANJANG<-----\nPersegi panjang dengan panjang {self.panjang}cm dan lebar {self.lebar}cm memiliki luas sebesar {self.hitung_luas_persegi_panjang()}cm^2"

if __name__ == "__main__":
    mhs = Mahasiswa()
    mhs.panjang = 20
    mhs.lebar = 12
    print(mhs.info_persegi_panjang())
