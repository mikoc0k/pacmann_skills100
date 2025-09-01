# case 1
# 1a,1b
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
            gaji_lembur = lembur * 30_000)
            print(f"\ntotal gaji lembur : int{gaji_lembur}")
            total = GAJI_KONTRAK + gaji_lembur
            print(f"gaji total : int{total}")
        elif (lembur > 20):
            gaji_lembur = 20 * 30_000
            print(f"\ntotal gaji lembur : int{gaji_lembur}")
            total = GAJI_KONTRAK + gaji_lembur
            print(f"gaji total : int{total}")
        else:
            print("jam tidak negatif)
"""