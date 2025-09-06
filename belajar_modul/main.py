import lingkaran
import persegi_panjang
import segitiga

def menu():
    print("1. Lingkaran")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("0. Keluar")
    print("Masukkan pilihan (1/2/3/0): ")

while True:
    menu()
    pilihan = input()

    if pilihan == '1':
        print(" pilih:\n a. luas \n b. keliling")
        sub_pilihan = input("Masukkan pilihan (a/b): ")
        if sub_pilihan == 'a':
            print("Luas Lingkaran:", lingkaran.luas_lingkaran())
        elif sub_pilihan == 'b':
            print("Keliling Lingkaran:", lingkaran.keliling_lingkaran())
    elif pilihan == '2':
        print(" pilih:\n a. luas \n b. keliling")
        sub_pilihan = input("Masukkan pilihan (a/b): ")
        if sub_pilihan == 'a':
            print("Luas Persegi Panjang:", persegi_panjang.luas_persegipanjang())
        elif sub_pilihan == 'b':
            print("Keliling Persegi Panjang:", persegi_panjang.keliling_persegipanjang())
    elif pilihan == '3':
        print(" pilih:\n a. luas \n b. keliling")
        sub_pilihan = input("Masukkan pilihan (a/b): ")
        if sub_pilihan == 'a':
            print("Luas Segitiga:", segitiga.luas_segitiga())
        elif sub_pilihan == 'b':
            print("Keliling Segitiga:", segitiga.keliling_segitiga())
    elif pilihan == '0':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")