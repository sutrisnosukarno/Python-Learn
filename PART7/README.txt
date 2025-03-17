Materi Belajar Array dalam Python

1. Pengertian Array

Array adalah struktur data yang digunakan untuk menyimpan sekumpulan nilai dalam satu variabel. Dalam Python, array bisa diimplementasikan menggunakan list atau dengan menggunakan modul array.

2. Perbedaan List dan Array

Penyimpanan
List: Dapat menyimpan berbagai tipe data
Array: Hanya dapat menyimpan satu tipe data

Kecepatan

List: Lebih lambat karena fleksibilitasnya
Array: Lebih cepat karena tipe data tetap

Modul

List: Built-in (langsung tersedia)
Array: Harus mengimpor modul array

3. Implementasi Array dalam Python

a. Menggunakan List

# Membuat list
angka = [1, 2, 3, 4, 5]
print(angka)

b. Menggunakan Modul array

import array

# Membuat array dengan tipe data integer
angka = array.array('i', [1, 2, 3, 4, 5])
print(angka)

Tipe data dalam array.array() ditentukan dengan kode berikut:

'i' : Integer

'f' : Float

'd' : Double

4. Operasi Dasar pada Array

a. Menambahkan Elemen

angka.append(6)  # Menambahkan elemen di akhir array
print(angka)

b. Menghapus Elemen

angka.remove(3)  # Menghapus elemen bernilai 3
print(angka)

c. Mengakses Elemen

print(angka[0])  # Mengakses elemen pertama

d. Mengubah Elemen

angka[1] = 10  # Mengubah elemen kedua menjadi 10
print(angka)

5. Iterasi dalam Array

a. Menggunakan Loop for

for num in angka:
    print(num)

b. Menggunakan while

i = 0
while i < len(angka):
    print(angka[i])
    i += 1

6. Fungsi dan Metode pada Array

Metode

Deskripsi

append(x)

Menambahkan elemen x di akhir array

insert(i, x)

Menyisipkan x pada indeks i

remove(x)

Menghapus elemen pertama yang bernilai x

pop(i)

Menghapus elemen pada indeks i (default: terakhir)

index(x)

Mengembalikan indeks pertama dari x

count(x)

Menghitung jumlah kemunculan x

reverse()

Membalik urutan array

sort()

Mengurutkan array

7. Contoh Program Lengkap

import array

# Membuat array
angka = array.array('i', [5, 2, 9, 1, 7])
print("Array Awal:", angka)

# Menambahkan elemen
angka.append(3)
print("Setelah append:", angka)

# Menghapus elemen
angka.remove(9)
print("Setelah remove:", angka)

# Mengakses elemen
print("Elemen pertama:", angka[0])

# Mengubah elemen
angka[2] = 10
print("Setelah update:", angka)

# Mengurutkan array
angka = sorted(angka)
print("Setelah sorting:", angka)

8. Kesimpulan

Array dalam Python bisa menggunakan list atau modul array.

List lebih fleksibel, sedangkan array lebih efisien untuk tipe data seragam.

Berbagai operasi dapat dilakukan pada array, seperti menambah, menghapus, mengakses, dan mengurutkan elemen.














import array

# Membuat array dengan tipe data integer
angka = array.array('i', [1, 2, 3, 4, 5])
print(angka)

# Menambahkan elemen di akhir array
angka.append(6)  
print(angka)

# menghapus elemen di  array
angka.remove(3)  
print(angka)

#mengakses elemen
print("elemen pertama: ", angka[0])

#mengubah elemen
angka[2] = 20
print("setelah update: ", angka)

#mengurutkan array
angka = sorted(angka)
print("setelah sorting: ", angka)