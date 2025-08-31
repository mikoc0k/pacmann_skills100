# Docstring :
# dokumentasi singkat ttg fungsi yang kita tulis
# format penulisan : """ ini adalah docstring """
# bisa multiline komentar
# contoh

def cetaknama(nama):
    """
    fungsi utk mencetak nama
    """
    print(f"nama saya: {nama}")

cetaknama("farhan kebab")

# menampilkan docstring dg cara help() atau __doc__.
# help(cetaknama)
# print(cetaknama.__doc__)

# contoh lain
def hitung_pangkat(num,power):
    """menghitung pangkat dari suatu angka"""
    pangkat = num ** power
    return pangkat

print(hitung_pangkat.__doc__)

# mini exercise
def hitung_pajak(penghasilan):
    """menghitung pajak dari penghasilan dengan persentase 10%"""
    pph = int(penghasilan * 0.1)
    return pph

print(hitung_pajak.__doc__)

# mini exercise
def props_negara(nama,area):
    """menampilkan nama dan proporsi negara terhadap luas permukaan bumi.

    Params:
    negara (string) : nama negara.
    luas (int) : luas negara.

    return:
    proporsi luas dibulatkan 2 angka dibelakang koma.
    
    """
    KONST = 148_950_000
    props = (area / KONST)*100
    hasil = print(f"Luas {nama} adalah {round(props,2)}% dari luas dunia")
    return hasil

props_negara("jepang",14_000_000)