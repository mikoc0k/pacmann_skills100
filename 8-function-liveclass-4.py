# 4
"""

def harga_pokok(beli_bersih, stok_awal, stok_akhir):
    hpp = beli_bersih + (stok_awal - stok_akhir)
    return hpp

"""

# 4A
# membuat docstring
def harga_poko(beli_bersih, stok_awal, stok_akhir):
    """
    fungsi menghitung HPP (harga pokok penjualan)
    
    Parameter :
    beli_bersih (int) : pembelian barang baru dalam setahun
    stok awal (int) : persediaan awal dalam setahun
    stok akhir (int) : persediaan akhir dalam setahun
    """
    hpp = beli_bersih + stok_awal - stok_akhir
    return hpp

# 4B fungsi ke dalam fungsi lambda
hpp = lambda beli_bersih, stok_awal, stok_akhir : beli_bersih + stok_awal - stok_akhir

# 4C
print(hpp(500_000,300_000,200_000)) 
