# 1a
# lingkaran.py
from math import pi
def luas_lingkaran(r):
    r = input("Masukkan jari-jari lingkaran: ")
    return pi * r * r

def keliling_lingkaran(r):
    r = input("Masukkan jari-jari lingkaran: ")
    return 2 * pi * r

# 1b
# persegi_panjang.py
def luas_persegipanjang(p,l):
    p = input("masukkan panjang: ")
    l = input("masukkan lebar: ")
    return p * l
def keliling_persegipanjang(p,l):
    p = input("masukkan panjang: ")
    l = input("masukkan lebar: ")
    return 2 * (p + l)

# 1c
# segitiga.py
def luas_segitiga(a,t):
    a = input("masukkan alas: ")
    t = input("masukkan tinggi: ")
    return 0.5 * a * t
def keliling_segitiga(a,b,c):
    a = input("masukkan sisi a: ")
    b = input("masukkan sisi b: ")
    c = input("masukkan sisi c: ")
    return a + b + c

# 1d
