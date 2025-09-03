# 2a
numbers = []
for i in range(10, -6, -2):
    numbers.append(i)
print(numbers)

# 2b
def hitung_rasio(deret):
    pos,neg,nul = 0,0,0
    for i in deret:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            nul += 1
    total = len(deret)
    return (f"{pos/total}\n{neg/total}\n{nul/total}")

print(hitung_rasio(numbers))