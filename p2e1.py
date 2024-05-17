class Segitiga:
  def __init__(self, nama, nim):
    self.nama = nama
    self.nim = nim

  def menu(self):
    print("\nPROGRAM MENGHITUNG KELILING & LUAS SEGITIGA")
    print("1. Keliling")
    print("2. Luas")

  def hitung_keliling(self):
    sisi1 = float(input("Masukan sisi 1: "))
    sisi2 = float(input("Masukan sisi 2: "))
    sisi3 = float(input("Masukan sisi 3: "))
    keliling = sisi1 + sisi2 + sisi3
    return keliling

  def hitung_luas(self):
    alas = float(input("Masukan alas: "))
    tinggi = float(input("Masukan tinggi: "))
    luas = 0.5 * alas * tinggi
    return luas

  def run(self):
    self.menu()
    pilihan = int(input("Masukan pilihan: "))

    if pilihan == 1:
      keliling = self.hitung_keliling()
      print(f"\nKeliling Segitiga: {keliling:.1f} cm")
    elif pilihan == 2:
      luas = self.hitung_luas()
      print(f"\nLuas Segitiga: {luas:.1f} cm^2")
    else:
      print("Pilihan tidak valid!")

    print("\nTerima kasih telah menggunakan program ini!")

# Example Usage
nama = input("Nama: ")
nim = input("NIM: ")
segitiga = Segitiga(nama, nim)
segitiga.run()
