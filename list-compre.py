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