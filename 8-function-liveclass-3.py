# 3a
voucher = 0.45
def hitung(*harga):
    total_sebelum_voucher = sum(harga)
    print(f"sebelum DISKON;{total_sebelum_voucher}")
    total = total_sebelum_voucher - (total_sebelum_voucher * voucher)
    print(f"setelah DISKON: {total}")
    return total
print(hitung(200_000,300_000,400_000,500_000,600_000,700_000))
