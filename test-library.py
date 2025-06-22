# Your code here
def discount_price(price,discount):
    final_price = price * (1-(discount/100))
    return f"Initial price: ${price:.2f}, Discount: {discount}%, Price after discount: {final_price:.2f} USD"

print(discount_price(100,5))
print(discount_price(86.5,2))
print(discount_price(50,0.5))