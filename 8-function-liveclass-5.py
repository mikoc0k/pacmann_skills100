# 5a
def show_data(**pegawai):
    for key,value in pegawai.items():
        print(f"{key} asal dari kota : {value}")

# 5b
show_data(irsyad="bekasi", chaidar="ternate", dwita="bali", fikria="malang", nurhaliza="yogyakarta")