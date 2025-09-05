# Modular Code
# teknik membagi tugas pemrograman besar menjadi komponen lebih kecil dan terpisah
# dapat digabung membentuk program yang lengkap

# Untuk dapat digunakan, file modul diimpor ke dalam file utama.

# Membuat modul
# konversi_jam.py
# fungsi konversi jam ke hari
def hari(jam):
    hari = jam // 24
    return f"{jam} jam = {hari} hari"

# fungsi konversi jam ke menit
def menit(jam):
    menit = jam * 60
    return f"{jam} jam = {menit} menit"

# fungsi konversi jam ke detik
def detik(jam):
    detik = jam * 3600
    return f"{jam} jam = {detik} detik"

# mini exercise
# membuat fungsi bunga_terendah
def bunga_tabungan(saldo,bunga):
    bunga = saldo * bunga * 30 / 365
    return round(bunga,2)
# membuat fungsi bunga anuitas
def bunga_anuitas(sisa_pinjaman, bunga):
    cicilan = sisa_pinjaman * bunga * 30
    return cicilan

# cara mengimpor modul
# import nama_modul
# contoh :
# import konversi_jam

# cara menggunakan fungsi dr modul yang diimport
# konversi_jam.hari(jam)

# ata cara kedua, mengimpor fungsi tertentu dari modul
# from nama_modul import nama_fungsi
# nama_fungsi()

# dengan cara import modul tertentu, kita juga dapat memanggil fungsi tertentu
# dipisahkan dengan koma

# cara lain, dengan mengimpor semua fungsi
# from nama_modul import *

# mengganti nama modul dan fungsi jika terlalu panjang
# dengan menggunakan alias "as"

# import nama_modul as nama_alias

# contoh mengubah nama fungsi
# from nama_modul import nama_fungsi as alias_fungsi

# mini exercise

# from modul_video_learning_materi_8.perhitungan_penjualan as penjualan import *
# profit(150,350_000,100_000)