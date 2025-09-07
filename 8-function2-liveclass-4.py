# soal 4a
# modul usaha.py
# fungsi-1 : beban usaha = bo + bno
def beban_usaha(bo, bno):
    bu = bo + bno
    return bu
#4b
# fungsi-2 : laba bersih = opcost + nonopcost - bu
def laba_bersih(opcost, nonopcost, bu):
    lb = opcost + nonopcost - bu
    return lb

# 4c 4d
print(beban_usaha(10_000_000, 3_500_000))

# 4e
print(laba_bersih(15_000_000, 7_000_000, 2_000_000))
