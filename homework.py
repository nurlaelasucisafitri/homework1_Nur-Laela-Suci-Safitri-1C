print("Makanan Layak Untuk Pasien")

Nama = input('Masukkan Nama_Pasien :')
Kondisi = input('Masukkan Kondisi Medis Pasien :')
Umur = int(input('Masukkan Umur :'))
Makanan = input('Makanan : ')

Status = ['nasi merah', 'kacang-kacangan', 'kentang', 'tempe', 'tahu', 'ayam tanpa kulit']
if Makanan not in Status :
    print ('tidak boleh dimakan')
else:
    print('boleh dimakan')

print('Semoga Cepat Sembuh')