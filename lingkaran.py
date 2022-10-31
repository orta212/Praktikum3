import math


print("\nNama : Orta Yamaesa")
print("NIM  : 312210147")
print("Kelas: TI.22.B1")
print("==============================================\n")
# print("Jari-jari lingkaran : %i" %(r))
r = float(input("masukan jari jari lingkaran : "))
# luas dan keliling lingkaran
luas = math.pi * r * r
keliling = 2 * math.pi * r
print('luas lingkaran : {0:f}'.format(luas))
print('keliling lingkaran : {0:f}'.format(keliling))