# 3a
belanja_surti = [20_000,80_000,40_000,150_500]
belanja_mima = [31_000, 43_000, 65_000, 105_000]
belanja_rani = [12_000, 200_000, 61_000,10_000]

# 3b
# belanja ibu surti
total_belanja_surti = sum(belanja_surti)
print("Total belanja ibu surti adalah Rp", total_belanja_surti)

# cara pacmann.io
"""
counter = 0
total_surti = 0
while counter < len(belanja_surti):
    total_surti += belanja_surti[counter]
    counter += 1
print("Total belanja ibu surti adalah Rp", total_surti)
"""

# 3c
disc_A = 0.01
disc_B = 0.03
harga_potongan = []
for item in belanja_surti:
    if item > 100_000:
        potongan = item * disc_B
    elif item > 50_000 and item <= 100_000:
        potongan = item * disc_A
    else:
        potongan = 0
    harga_potongan.append(item - potongan)
print(harga_potongan)
print("Total belanja ibu surti setelah diskon adalah Rp", sum(harga_potongan))

# jawaban pacmann.io
"""
counter = 0
total_ibu_surti = 0
potongan = 0
while counter < len(belanja_surti):
    if belanja_surti[counter] > 50_000 and belanja_surti[counter] < 100_000:
    potongan = belanja_surti[counter] * 1%
    harga_final = belanja_surti[counter] - potongan
    elif belanja_surti[counter] > 100_000:
    potongan = belanja_surti[counter] * 3%
    harga_final = belanja_surti[counter] - potongan
    else:
    harga_final = belanja_surti[counter]
    total_ibu_surti += harga_final
    counter += 1
print("Total belanja ibu surti setelah diskon adalah Rp", total_ibu_surti
"""