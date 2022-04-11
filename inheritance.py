class barang:
  def __init__(self, barang, harga):
    self.barang = barang
    self.harga = harga
 
  def printname(self):
    print(self.barang, 'Harga : Rp.' ,self.harga)

class pakaian(barang):
  pass

pakaian1 = pakaian("Daster", "120000")
pakaian1.printname()
pakaian1 = pakaian("Almamater", "200000")
pakaian1.printname()
