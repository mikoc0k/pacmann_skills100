# fungsi = kode yang bisa dipakai berkali kali
def perkalian(a, b):
    print(f"{a} x {b} = {a * b}")

perkalian(2, 3)
perkalian(5, 6)
perkalian(10, 4)

# DRY = Don't Repeat Yourself
# ----------------------------------------------- #

# mini exercise
def fungsi_teks():
    print('saya sedang belajar fungsi di python')

fungsi_teks()

# fungsi dengan parameter = inputan fungsi

def identf(nama):
    print(nama)

identf("jowokee")

# fungsi dengan beberapa params

def identfs(nama,asal,umur):
    print(f'nama saya {nama} asal {asal} dan umur saya {umur} tahun')

identfs("owok","neraka", 99)