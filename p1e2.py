class NilaiHuruf:
  def _init_(self, nilai):
    self.nilai = nilai
  
  def get_name(nama,id):
    return nama,id

  def get_huruf(self):
    if self.nilai >= 80:
      return "A"
    elif self.nilai >= 77:
      return "A-"
    elif self.nilai >= 74:
      return "B+"
    elif self.nilai >= 68:
      return "B"
    elif self.nilai >= 65:
      return "B-"
    elif self.nilai >= 62:
      return "C+"
    elif self.nilai >= 56:
      return "C"
    elif self.nilai >= 45:
      return "D"
    else:
      return "E"


nama= input('Nama: ')
nim = input('nim: ')
nilai = float(input("Masukkan nilai: "))
nilai_huruf = NilaiHuruf(nilai)

huruf = nilai_huruf.get_huruf()
print(f'\n---  DATA PRAKTIKAN PBO 2024  ---')
print(f"Nama: {nama}\nNim: {nim}")
print(f"Grade: {huruf}")