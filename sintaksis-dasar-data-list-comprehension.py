"""
Sintaksis dasar dalam bentuk data list comprehension
"""

print('daftar buku :')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
print(daftar_buku)

print('\nperintah del simple pada elemen ke-2')
del daftar_buku[1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# START:END

print('\nperintah del dengan data list comprehension #START:END')
del daftar_buku[:] #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\ndi urutan elemen ke [0:3]')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
del daftar_buku[0:3] #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\ndi urutan elemen ke [0:-3]')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
del daftar_buku[0:-3] #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# START:END:STEP

print('\nperintah del dengan data list comprehension #START:END')
print('\ndi urutan elemen ke [0::2]')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
del daftar_buku[0::2] #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\ndi urutan elemen ke [0::-1]')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
del daftar_buku[0::-1] #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Membuat List Baru [:]

print('\nperintah del dengan data list comprehension')

print('\nmembuat list baru yang sudah di del')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']

daftar_buku_baru = daftar_buku[:]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# Perintah del dengan list comprehension GANJIL:GENAP

print('\nperintah del dengan list comprehension #GANJIL')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
del daftar_buku[0::2] #start:stop:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension #GENAP')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
del daftar_buku[1::2] #start:stop:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension #buang di ujung tertentu')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
del daftar_buku[0:-1:2] #start:stop:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension #tanpa for in')
daftar_buku = ['1. seven habits', '2. how to influence people', '3. first thing fist', '4. 4dx']
print(daftar_buku[0::2])
print(daftar_buku[1::2])
print(daftar_buku[0:-1:2])
