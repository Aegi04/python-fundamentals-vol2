"""
Dasar sintaksis dalam pemograman python terdiri dari :
1. Sekuential = Langkah Berurutan
2. Branching / Percabangan = Langkah lompatan jika kondisi terpenuhi
3. Looping / Perulangan =  Mengulang langkah yang sama secara berkali - kali
selama atau sampai kondisi terpenuhi
"""

# Sekuential

print('Seorang Ibu meminta tolong kepada anaknya'
      '\nyaitu Budi untuk membelikan 2 botol susu'
      '\ndan 6 butir telor ke Toko')

print('\nIbu berkata : "Pergi ke Toko"')
print('Budi menjawab : " Baik Bu, apa yang harus Saya lakukan di toko?"')
print('Ibu berkata : " Tolong belikan Ibu 2 botol susu dan 6 butir telor"')
print('dan ini uangnya!')
print('Budi menjawab : "Baik Bu."')
print('Kemudian Budi berangkat ke Toko dan segera membelikannya.')

# Percabangan

jumlah_botol_susu = 10
print(f'\njumlah botol susu {jumlah_botol_susu}')
jumlah_telor = 150
print(f'jumlah telor {jumlah_telor}')

if jumlah_botol_susu > 0:
    print('\nBudi pergi ke Toko dan')
    print('Budi membeli 2 botol susu')

    if jumlah_telor == 0:
        print('Budi tidak membeli dengan Telornya')
    else:
        print('serta Budi membeli 6 butir telor juga')

else:
    print('Budi tidak jadi beli susunya')

print('\nSetelah itu Budi pulang ke rumah'
      '\ndan memberikan belanjaannya kepada Ibunya.')
