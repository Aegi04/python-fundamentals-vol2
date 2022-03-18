"""
Sintaksis dasar dalam tipe data list ;
"""
daftar_buku = ['seven habits', 'how to influence people', 'first thing fist', '4dx']
print('\ntampilkan variabel daftar buku')
print(daftar_buku)

print('\nproses semua daftar buku dengan for in')
for buku in daftar_buku:
    print(buku)

print('\ntampilkan isi daftar buku pada index tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\ntampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\ntampilkan dengan for in range,'
      'dimana tipe data tiap elemen berbeda-beda')
daftar_buku_vol2 = ['biologis', '204', '0,36', '-76']
for i in range(0, len(daftar_buku_vol2)):
    print(daftar_buku_vol2[i])

print('\nkembalikan nilai awal daftar buku')
print(daftar_buku)

print('\ntambahkan 1 buku baru')
daftar_buku.append('biologis')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nclear list')
daftar_buku.clear()

print('\nganti elemen pertama pada daftar buku jadi (eight habits)')
daftar_buku = ['seven habits', 'how to influence people', 'first thing fist', '4dx']
daftar_buku[0] = 'eight habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nambil elemen ke-2 dari daftar buku')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nbuku yang di ambil tadi')
print(buku)

# Tabel pop lengkap

print('\ntabel pop lengkap')
daftar_buku = ['seven habits', 'how to influence people', 'first thing fist', '4dx']
daftar_buku.pop(0)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n')
daftar_buku = ['seven habits', 'how to influence people', 'first thing fist', '4dx']
daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n')
daftar_buku = ['seven habits', 'how to influence people', 'first thing fist', '4dx']
daftar_buku.pop(3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
