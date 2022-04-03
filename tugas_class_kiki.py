#kiki malinda_D0219340
class mahasiswa():
    jurusan = "teknik informatika"
 
    def __init__(self, input_nama):
        self.nama = input_nama # public
 
kiki = mahasiswa("kiki malinda")
 
print(mahasiswa.jurusan)
print(kiki.jurusan)
