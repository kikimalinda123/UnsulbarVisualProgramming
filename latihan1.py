class Mahasiswa:
    def __init__(self, inputNama, inputNim, inputAngkatan):
        self.nama = inputNama
        self.nim = inputNim
        self.angkatan = inputAngkatan

Teknik1 = Mahasiswa("Kiki Malinda", "D0219340", 2019)
Sipil1 = Mahasiswa("Fitri", "F0118933", 2018)

print (Teknik1.nama)
