# Tugas Pertemuan 6 Praktikum 3 <hr> <br>

## Daftar isi 
1. [Latihan 1](#Latihan-1)
2. [Latihan 2](#Latihan-2)
3. [Latihan 3](#Latihan-3)

# Latihan 1
<br>
* buat Source Code <br>

![SC latihan1](https://user-images.githubusercontent.com/47426095/198815060-adb529f3-1b8f-478c-aa5c-84292c55e64c.png)
```python 
#penggunaan end
print('A', end=' ')
print('B', end=' ')
print('C', end=' ')
print()
print('X')
print('Y')
print('Z')

# penggunaan separator
w,x,y,z = 10,15,20,25
print(w,x,y,z)
print(w,x,y,z, sep = ',')
print(w,x,y,z, sep = '')
print(w,x,y,z, sep = ':')
print(w,x,y,z, sep = '-----')

#string format
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

#string format
print('{0:3} {1:>16}'.format(0, 10**0))
print('{0:3} {1:>16}'.format(1, 10**1))
print('{0:3} {1:>16}'.format(2, 10**2))
print('{0:3} {1:>16}'.format(3, 10**3))
print('{0:3} {1:>16}'.format(4, 10**4))
print('{0:3} {1:>16}'.format(5, 10**5))
print('{0:3} {1:>16}'.format(6, 10**6))
print('{0:3} {1:>16}'.format(7, 10**7))
print('{0:3} {1:>16}'.format(8, 10**8))
print('{0:3} {1:>16}'.format(9, 10**9))
print('{0:3} {1:>16}'.format(10, 10**10))
```

* Lakukan Run File
* Hasil Output : <br>
![run latihan1](https://user-images.githubusercontent.com/47426095/198815125-3cfb5640-7129-460c-a8a2-99435eb5272a.PNG)
<br>
```
A B C 
X
Y
Z
10 15 20 25
10,15,20,25
10152025
10:15:20:25
10-----15-----20-----25
0 1
1 10
2 100
3 1000
4 10000
5 100000
6 1000000
7 10000000
8 100000000
9 1000000000
10 10000000000
  0                1
  1               10
  2              100
  3             1000
  4            10000
  5           100000
  6          1000000
  7         10000000
  8        100000000
  9       1000000000
 10      10000000000
 ```
