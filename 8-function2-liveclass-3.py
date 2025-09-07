# 3a
info = {
    "prod_cost" : 35_000,
    "sell_price" : 50_000,
    "qty" : 1200,
    "stok" : 100
}

print(info)

# 3b 3c
# fungsi-1 : hitung untung < qty * (sell_price - prod_cost ) >
# fungsi-2 : hitung harga pokok < prod_cost + qty - stok>
def calc_profit(data):
    prod_cost = data["prod_cost"]
    sell_price = data["sell_price"]
    qty = data["qty"]
    profit = qty * (sell_price - prod_cost)
    return profit

def calc_baseprice(data):
    prod_cost = data["prod_cost"]
    qty = data["qty"]
    stok = data["stok"]
    base_price = prod_cost + qty - stok
    return base_price

#3d
print(calc_profit(info))
print(calc_baseprice(info))
