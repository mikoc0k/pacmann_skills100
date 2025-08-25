"""
nama barang     | jumlah
sandal angsa    | 4
mie seleraku    | 15
kopi putih      | 20
kopi kapal karam | 12
sabun kehidupan | 7
sampo matahari  | 11
lombok cap gajah | 3
bawang merah    | 2
bawang putih    | 3
kecap EFG      | 6
"""

daftar_harga = [
    ['sandal angsa', 4],
    ['mie seleraku', 15],
    ['kopi putih', 20],
    ['kopi kapal karam', 12],
    ['sabun kehidupan', 7],
    ['sampo matahari', 11],
    ['lombok', 3],
    ['bawang merah', 2],
    ['bawang putih', 3],
    ['kecap EFG', 6]
]
print(daftar_harga)

# 5b
keranjang_kecil = []
for barang, jumlah in daftar_harga:
    if jumlah < 5:
        keranjang_kecil.append(barang)
print(f'keranjang_kecil: {keranjang_kecil}')