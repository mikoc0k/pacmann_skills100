# 2 perhitungan bunga
# perhitungan_angsuran_per_bulan_klien.py
# modul legacy

# fungsi bunga anuitas
def bunga_anuitas(pinjaman, bunga):
    DAYS = 30
    tabungan = pinjaman * bunga * DAYS
    return tabungan

# fungsi bunga flat
# 2a
def bunga_flat(pinjaman, bunga):
    MONTHS = 12
    RATES = 0.1
    base_pinjaman = pinjaman / MONTHS
    rates_year = pinjaman * RATES
    rates_month = rates_year / MONTHS
    total_angsuran = print(f"angsuran per bulan: {int(base_pinjaman + rates_month)}")
    return total_angsuran

# 2b
# import perhitungan_angsuran_per_bulan_klien as perhitungan_bunga

# 2c
bunga_flat(10_000_000,0.1)