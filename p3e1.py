class Mahasiswa:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi



    def __str__(self):
        return f"{self.nama} {self.nim}\n-----PROGRAM MENAMPILKAN IDENTITAS-----\nNama saya adalah {self.nama} NIM saya {self.nim}. \nSaya dari fakultas {self.fakultas}. \nHobi saya adalah {self.hobi}"
    
mhs = Mahasiswa("Agfan Herru Pratama Hendarsin", "(064002100043)", "Teknik Informatika", "Ngelamun di WC")

print(mhs)