mahasiswa = {
  'nama': 'Feri Maulana',
  'asal': 'Indonesia'
}

# mengubah data
print('Nama awal:', mahasiswa.get('nama'))
mahasiswa['nama'] = 'Andi Ali'
print('Setelah diubah:', mahasiswa.get('nama'))