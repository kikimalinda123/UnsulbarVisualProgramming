#kiki malinda_D0219340
class private():
    __items = 4 # private
 
    def __init__(self, nama_barang):
        self.nama = nama_barang
 
    def harga_barng(self,harga_barang):
       hasil = self.__items * harga_barang
       return hasil
 
celana = private("celana panjang")
print(celana.harga_barng(100))
