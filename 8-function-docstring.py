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