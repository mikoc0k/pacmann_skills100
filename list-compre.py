# List comprehension
# membuat list baru dari list yang sudah ada, dg lebih sederhana
# berisi 3 komponen : for loop + kondisi/ ekspresi + output

# cara konvensional
daftar_gaji = [2_000_000, 3_500_000, 4_500_000,2_900_000]
daftar_gaji_baru = []
# for loop biasa
for gajian in daftar_gaji :
    daftar_gaji_baru.append(gajian)

print("cara konv- : ",daftar_gaji_baru)

# cara List comprehension
daftar_gaji_baru_compre = [gaji for gaji in daftar_gaji]
print("cara list compre- : ",daftar_gaji_baru_compre)

# dengan List comprehension, kita bisa langsung memanipulasi output
daftar_gaji_bagi_5 = [gaji/5 for gaji in daftar_gaji]
print("hasil daftar gaji / 5 : ",daftar_gaji_bagi_5)

# memberi syarat lalu mencetak
gaji_lebih_dari_3000k = [gaji for gaji in daftar_gaji if gaji > 3_000_000]
print("gaji > 3juta : ",gaji_lebih_dari_3000k)

# contoh lain
nilai_kelas_a = [55,60,60,77,89,40,44,90]
nilai_lulus = [nilai for nilai in nilai_kelas_a if nilai > 70]
print("nilai lulus >70 : ",nilai_lulus)

# membuat list baru tanpa list yang ada sebelumnya

# cara konven
list_baru = []
for angka in range(0,10):
    list_baru.append(angka)

print("list konven : ",list_baru)

# cara list comprehen
list_baru_comprehen = [angka for angka in range(0,10)]
print("list komprehen", list_baru_comprehen)