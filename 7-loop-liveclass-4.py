# 4A
kendaraan_record = (('Q 1113 OP', 'Mobil', 'Jalur A'), ('BZ 9008 IQ', 'Mobil', 'Jalur A'),
              ('U 3233 JK', 'Mobil', 'Jalur A'), ('YT 8809 SH', 'Ambulance', 'Jalur A'),
              ('UX 1124 IU', 'Mobil', 'Jalur B'), ('BZ 7672 UI', 'Mobil', 'Jalur B'),
              ('YT 1123 XY', 'Mobil', 'Jalur B'), ('YY 1121 YY', 'Mobil', 'Pemadam Kebakaran' )
              )
print(kendaraan_record)

# 4B
"""
jenis plat ---- jalur
Plat ganjil ---- Jalur A
Plat genap ---- Jalur B

"""
kecuali = ['Ambulance','Pemadam Kebakaran']
for plat,jenis,jalur in kendaraan_record:
    nomor=plat[-4]
    if int(nomor) %2 != 0 and jalur == 'Jalur A':
        continue
    elif int(nomor) %2 == 0 and jalur == 'Jalur B':
        continue
    elif jalur in kecuali:
        continue
    else:
        print(f'{jenis} dengan plat {plat} masuk {jalur} | kena e-tilang')