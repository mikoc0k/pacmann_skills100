menu = [    
        "telur rebus",
        "ikan goreng",
        "tahu tempe"
]

i = 0
for tanggal in range(1,31):
    if tanggal % 7 == 0:
        print(f"tanggal {tanggal} adalah hari libur")
        continue
    print(f" menu tanggal-{tanggal} : nasi & {menu[i]}")
    i += 1
    if i >= len(menu):
            i = 0