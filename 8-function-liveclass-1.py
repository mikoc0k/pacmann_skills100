# case 1
# 1a,1b
"""

def kategori():
    value = input("pilih kategori pegawai: (tetap/kontrak)? \n")
    lembur = input("isi jam lembur:")
    if value == "tetap":
        if int(lembur) > 20:
            lembur = 20
        else:
            lembur = int(lembur)
        print(f"total gaji lembur: {lembur*50_000}")
        print(f"gaji total = {((lembur*50_000) + 4_500_000)}")
    else :
        print(f"total gaji lembur: {lembur*25_000}")
        print(f"gaji total = {((lembur*25_000) + (0.7* 4_500_000))}")
kategori()

"""
# versi pacmann.io
""""
def hit_penghasilan():
    kategori = input("pilih kategori : tetap/ kontrak ? ")
    lembur = float(input("isi jam lembur : "))
    GAJI_TETAP = 4_500_000
    GAJI_KONTRAK = .7 * 4_500_000

    if (kategori == "tetap" or kategori == "Tetap"):
        if (lembur >= 0 and lembur <= 20):
            gaji_lembur = lembur * 50_000
            print(f"\ntotal gaji lembur : int{gaji_lembur}")
            total = GAJI_TETAP + gaji_lembur
            print(f"gaji total : int{total}")

        elif (lembur > 20):
            gaji_lembur = 20 * 50_000
            print(f"\ntotal gaji lembur : int{gaji_lembur} ")
            total = GAJI_TETAP + gaji_lembur
            print(f"gaji total : int{total}")
        
        else:
            print("jam lembur tidak boleh negatif")
    elif (kategori == "kontrak" or kategori == "Kontrak"):
        if (lembur >= 0 and lembur <= 20):
            gaji_lembur = lembur * 30_000
            print(f"\ntotal gaji lembur : int{gaji_lembur}")
            total = GAJI_KONTRAK + gaji_lembur
            print(f"gaji total : int{total}")
        elif (lembur > 20):
            gaji_lembur = 20 * 30_000
            print(f"\ntotal gaji lembur : int{gaji_lembur}")
            total = GAJI_KONTRAK + gaji_lembur
            print(f"gaji total : int{total}")
        else:
            print("jam tidak negatif")
"""
# 1c
def kategori():
    value = input("pilih kategori pegawai: (tetap/kontrak)? \n").lower()
    try:
        lembur = float(input("isi jam lembur: "))
    except ValueError:
        print("jam lembur harus berupa angka")
        return
    GAJI_TETAP = 4_500_000
    GAJI_KONTRAK = .7 * GAJI_TETAP

    if value == "tetap":
        tarif = 50_000
        gaji_pokok = GAJI_TETAP
    elif value == "kontrak":
        tarif = 30_000
        gaji_pokok = GAJI_KONTRAK
    else:
        print("kategori tidak valid")
        return
    
    if lembur < 0:
        print("jam lembur tidak boleh negatif")
        return
    
    jam_lembur = min(lembur, 20)
    gaji_lembur = jam_lembur * tarif
    total_gaji = gaji_pokok + gaji_lembur
    total_pasca_pajak = total_gaji * 0.99
    print(f"total gaji lembur: {gaji_lembur}")
    print(f"gaji total: {total_gaji}")
    print(f"total gaji setelah pajak: {total_pasca_pajak}")

kategori()