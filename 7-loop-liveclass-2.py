# 2a ------------------------------------------ #
list_vltr = []
for vltr in range(1,201):
    """
    mengambil urutan kelipatan 5 dan 7 dari 1 sampai 200
    lalu mengambilnya dari urutan ke-2 dari belakang"""
    if vltr % 7 == 0 and vltr % 5 == 0:
        list_vltr.append(vltr)
print(list_vltr[-2])

# jawaban versi pacmann.io
"""
penonto_terpilih = []
penonton = 100
angka = 1
while angka <= penonton:
    if angka % 5 == 0 and angka % 7 == 0:
        penonto_terpilih.append(angka)
    angka += 1
print(penonto_terpilih[-2])
"""
# ------------------------------------------ #

# 2b ------------------------------------------ #

list_voltr = []
for voltr in range(1,50):
    if voltr % 11 == 0 :
        list_voltr.append(voltr)
print(list_voltr[1])

# jawaban versi pacmann.io
"""
penonton_terpilih = []
angka = 1
while angka < 50:
    if angka % < 50 and angka % 11 == 0:
        penonton_terpilih.append(angka)
    angka += 1
print(penonton_terpilih[1])         
"""
# ------------------------------------------- #


# 2c
daftar_volunt = []
for angka in range(50, 101):
    if angka % 8 == 0:
        daftar_volunt.append(angka)
print(daftar_volunt[-1])

# jawaban versi pacmann.io
"""
penonton_terpilih = []
angka = 1
while angka <= 100:
    if angka >= 50 and angka % 8 == 0:
        penonton_terpilih.append(angka)
    angka += 1
print(penonton_terpilih[-1])
"""
# ------------------------------------------- #