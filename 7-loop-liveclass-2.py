list_vltr = []
for vltr in range(1,201):
    """
    mengambil urutan kelipatan 5 dan 7 dari 1 sampai 200
    lalu mengambilnya dari urutan ke-2 dari belakang"""
    if vltr % 7 == 0 and vltr % 5 == 0:
        list_vltr.append(vltr)
print(list_vltr[-2])