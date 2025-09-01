# Lambda adalah fungsi tanpa nama (anonymous)
# jika fungsi didefinisikan dengan def
# maka lambda didefinisikan dengan lambda

# contoh fungsi lambda
sapa = lambda nama: print(f"hallo {nama}")
sapa("farhan kebab")

# format penulisan lambda
# lambda <params>: <isi fungsi>

# contoh lain
kuadrat = lambda angka: angka**2 # karna lambda tidak punya nama maka perlu var kuadrat utk simpan nilai
print(kuadrat(2)) # baris hanya 1, tidak bs lebih
# ekspresi juga cm 1

# contoh lagi
profit = lambda income, cost: income - cost
print(profit(100_000,50_500))

# mini exercise
harga_diskon = lambda qty,price,disc: qty * price * (1-disc)
print(harga_diskon(2,1_000_000,0.15))

# fungsi lambda untuk percabangan
hitung = lambda num: num+1 if num < 10 else 2*num
print(hitung(10))
print(hitung(5))

# mini exercise
cuti = lambda lembur, bolos: print("boleh cuti") if lembur >=8 and bolos < 4 else print("no cuti !")
cuti(10,3)
cuti(4,5)

# mini exercise
margin_kotor = lambda laba,incom : print(f" margin kotor - {int(laba / incom * 100)}%")
margin_kotor(150_000,250_000)