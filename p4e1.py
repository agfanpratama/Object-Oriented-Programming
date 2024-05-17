class Student:
    # Deklarasi variabel (instance & class)
    data_pribadi = "--- Data Pribadi ---"  # variabel class

    # Constructor untuk inisialisasi objek Student
    def __init__(self, nama):
        self.nama = nama
        self.nim = None
        self.nilai = None

    # Method untuk mengatur NIM
    def set_nim(self, nim):
        self.nim = nim

    # Method untuk mengatur nilai
    def set_nilai(self, nilai):
        self.nilai = nilai

    # Method untuk mencetak data siswa
    def print_data(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Nilai:", self.nilai)

    # Method untuk mencetak data teman dengan nomor tertentu
    @staticmethod
    def print_data_teman(nomor_teman, teman):
        print("--- Data Teman", nomor_teman, "---")
        teman.print_data()


# Blok kode utama
if __name__ == "__main__":
    # Pemanggilan method static (data pribadi)
    
    # Pembuatan Objek
    murid1 = Student("Gagah Putra B")
    murid2 = Student("Agfan Herru Pratama H")
    murid3 = Student("I Made N A")
    murid4 = Student("Nathanael W")

    # Pengaksesan method nim dan nilai
    pribadi = Student.data_pribadi
    print(pribadi)
    murid1.set_nim("064002100036")
    murid1.set_nilai(100)

    murid2.set_nim("064002100043")
    murid2.set_nilai(99)

    murid3.set_nim("064002100020")
    murid3.set_nilai(95)

    murid4.set_nim("064002100030")
    murid4.set_nilai(80)

    # Cetak detail siswa
    murid1.print_data()
    Student.print_data_teman(1, murid2)
    Student.print_data_teman(2, murid3)
    Student.print_data_teman(3, murid4)

