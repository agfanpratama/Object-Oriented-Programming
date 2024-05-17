class Awal:
    def __init__(self, gaji, golongan):
        self.gaji = gaji
        self.golongan = golongan

    def print_gaji(self):
        print("Golongan", self.golongan, "Mendapatkan Gaji:", self.gaji)


class Dosen(Awal):
    def __init__(self, gaji, golongan):
        super().__init__(gaji, golongan)

    def print_gaji(self):
        print("Golongan", self.golongan, "Mendapatkan Gaji:", self.gaji + 300000)


class Staff(Awal):
    def __init__(self, gaji, golongan):
        super().__init__(gaji, golongan)

    def print_gaji(self):
        print("Golongan", self.golongan, "Mendapatkan Gaji:", self.gaji * 2)


class Lainnya(Awal):
    def __init__(self, gaji, golongan):
        super().__init__(gaji, golongan)

    def print_gaji(self):
        print("Golongan", self.golongan, "Mendapatkan Gaji:", self.gaji)




def main():
    dosen = Dosen(150000, "DOSEN")
    staff = Staff(150000, "STAFF")
    lainnya = Lainnya(150000, "LAINNYA")
    nama = 'Agfan Herru Pratama Hendarsin'
    nim = '064002100043'
    print(f"===========================\nNama: {nama} ||\n Nim: {nim}       ||\n===========================")
    dosen.print_gaji()
    staff.print_gaji()
    lainnya.print_gaji()
    


if __name__ == "__main__":
    main()
