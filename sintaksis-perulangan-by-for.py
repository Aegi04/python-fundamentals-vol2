"""
Program sintaksis perulangan membaca buku dengan For
"""
print('Program sintaksis perulangan membaca buku dengan For')

# Perulangan by For

jumlah_buku = 10
print(f'\nJumlah buku {jumlah_buku}')
jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print('\nIbu menyuruh Budi untuk membaca semua bukunya')
for jumlah_buku_yang_sudah_dibaca in range (1, jumlah_buku+1):
    print(f'Buku ke {jumlah_buku_yang_sudah_dibaca} telah dibaca')

print(f'\nJadi jumlah total buku yang telah dibaca'
      f'\noleh Budi adalah {jumlah_buku_yang_sudah_dibaca} buku')
