Kondisi di Python dan Pernyataan If

Python mendukung kondisi logis yang biasa dari matematika:
Sama dengan: a == b
Tidak Sama dengan: a != b
Kurang dari: a < b
Kurang dari atau sama dengan: a <= b
Lebih besar dari: a > b
Lebih besar dari atau sama dengan: a >= b

Kondisi ini dapat digunakan dalam beberapa cara, paling umum dalam "pernyataan if" dan loop.
Sebuah "pernyataan if" ditulis dengan menggunakan kata kunci if.

contoh if1.py

a = 33
b = 200
if b > a:
print("b lebih besar dari a")
===================================
Elif

Kata kunci elif adalah cara python untuk mengatakan "jika kondisi sebelumnya tidak benar, maka coba kondisi ini".

contoh if2.py
a = 33
b = 33
if b > a:
print("b lebih besar dari a")
elif a == b:
print("a dan b bernilai sama")
=================================
Else
Kata kunci else memproses apa pun yang tidak diproses oleh kondisi sebelumnya.

contoh if3.py

a = 200
b = 33
if b > a:
print("b lebih besar dari a")
elif a == b:
print("a dan b bernilai sama")
else:
print("a lebih besar dari b")
===================================


