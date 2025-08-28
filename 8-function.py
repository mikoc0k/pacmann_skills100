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

# fungsi return feat looping
def diskon(promo,harga):
    if promo == True:
        potongan = 0.5
        total_harga = int(harga*potongan)
        print(total_harga)
    else:
        print(harga)

diskon(True,100_000)
diskon(False,100_000)

# fungsi dengan loop dan list

def daftar_kriteria():
    list_kriteria = ["Menggunakan komputer", "Menggunakan laptop", "Menggunakan tablet"]
    for index in range(len(list_kriteria)):
        print(f"{index+1}. {list_kriteria[index]}")

daftar_kriteria()

# mini exercise

def jadwal_catering(hari):
    match hari:
        case "senin":
            print("nasi kuning")
        case "selasa":
            print("salad sayur")
        case "rabu":
            print("soto ayam")
        case "kamis":
            print("nasi goreng")
        case "jumat":
            print("rawon")
        case _:
            print("menu tidak tersedia")

jadwal_catering("rabu")
jadwal_catering("kamis")
jadwal_catering("jumat")
jadwal_catering("sabtu")

# jawaban pacmann.io

"""
def jadwal_catering(hari):
  if (hari == "Senin" or hari == "senin"):
    print("Menu makan hari Senin adalah Nasi Kuning.")

  elif (hari == "Selasa" or hari == "selasa") :
    print("Menu makan hari Selasa adalah Salad Sayur.")

  elif (hari == "Rabu" or hari == "rabu") :
    print("Menu makan hari Rabu adalah Soto Ayam.")

  elif (hari == "Kamis" or hari == "kamis") :
    print("Menu makan hari Kamis adalah Nasi Goreng.")

  elif (hari == "Jumat" or hari == "jumat") :
    print("Menu makan hari Jumat adalah Rawon.")
    
  else :
    print("Menu makan tidak tersedia.")

"""

# argumen harus diisi berurutan sesuai dengan parameter fungsinya
# namun dapat diisi secara bebas urutan dengan cara keyword argument

def idtf(nama, asal, umur):
    print(f'nama saya {nama} asal {asal} dan umur saya {umur} tahun')

idtf(umur=669, nama="owok", asal="neraka")

# mini exercise

def pegawai(nama, departemen, tahun):
    print(f"{nama}, merupakan karyawan dari departemen {departemen} sejak tahun {tahun}")

pegawai("chaidar", "publik relasi", 2014)
pegawai(departemen="publik relasi", tahun=2014, nama="chaidar")

# default Value
# parameter dg nilai konstan

def area_circle(jari_jari, phi=3.14):
    luas = phi * jari_jari * jari_jari
    print(f"luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")

area_circle(10)

# mini exercise

def luas(panjang,lebar=5):
    luas = panjang * lebar
    print(f"luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

luas(3)