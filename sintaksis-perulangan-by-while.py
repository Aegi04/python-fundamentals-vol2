"""
Program sintaksis perulangan dasar dengan While
"""
print('Program sintaksis perulangan dasar dengan While')

# Perulangan by While

print('\nDiketahui :')
jumlah_buku = 10
print(f'Jumlah buku {jumlah_buku}')

jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

jumlah_buku_yang_sudah_paham = 0
print(f'Jumlah buku yang sudah dipahami {jumlah_buku_yang_sudah_paham}')

print('\nIbu menyuruh Budi untuk membaca semua bukunya')
print('sampai paham, maka:')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca+1
    print(f'Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

    if jumlah_buku_yang_sudah_paham > 6:
        print(f'Tetapi belum paham')
    else:
        jumlah_buku_yang_sudah_paham = jumlah_buku_yang_sudah_paham+1
        print('dan telah dipahami')

print(f'\nJadi total buku yang sudah dibaca itu ada {jumlah_buku_yang_sudah_dibaca}'
      f'\ntapi yang telah dipahami itu semuanya cuman ada {jumlah_buku_yang_sudah_paham}')
