Tutorial Fungsi dengan Argumen di Python

1. Pengertian Fungsi dengan Argumen

Fungsi dengan argumen di Python adalah fungsi yang menerima nilai saat dipanggil. Nilai ini disebut sebagai argumen dan digunakan dalam proses di dalam fungsi.

2. Cara Membuat Fungsi dengan Argumen

Untuk mendefinisikan fungsi dengan argumen, gunakan kata kunci def, diikuti dengan nama fungsi dan daftar argumen dalam tanda kurung.

# Contoh fungsi dengan satu argumen
def sapa(nama):
    print(f"Halo, {nama}! Selamat datang.")

# Pemanggilan fungsi
sapa("Andi")

3. Fungsi dengan Beberapa Argumen

Fungsi dapat memiliki lebih dari satu argumen.

# Contoh fungsi dengan dua argumen
def tambah(a, b):
    return a + b

# Pemanggilan fungsi
nilaiku = tambah(3, 5)
print("Hasil penjumlahan nilaiku:", nilaiku)

4. Argumen Default

Argumen dapat memiliki nilai default jika tidak diberikan saat pemanggilan fungsi.

# Contoh fungsi dengan argumen default
def salam(nama, pesan="Selamat pagi"):
    print(f"{pesan}, {nama}!")

# Pemanggilan fungsi
salam("Budi")
salam("Ani", "Selamat sore")

5. Argumen Keyword (Keyword Arguments)

Saat memanggil fungsi, kita bisa menentukan nilai argumen berdasarkan nama parameter.

# Contoh penggunaan keyword arguments
def biodata(nama, usia, kota):
    print(f"Nama: {nama}, Usia: {usia}, Kota: {kota}")

# Pemanggilan dengan keyword arguments
biodata(nama="Citra", kota="Bandung", usia=25)

6. Argumen Dinamis (*args dan **kwargs)

*args (Non-keyword Arguments)

Digunakan untuk menerima sejumlah argumen yang tidak ditentukan sebelumnya.

# Contoh penggunaan *args
def jumlahkan(*angka):
    return sum(angka)

# Pemanggilan fungsi
print(jumlahkan(1, 2, 3, 4, 5))

**kwargs (Keyword Arguments)

Digunakan untuk menerima argumen dalam bentuk pasangan kunci-nilai (dictionary).

# Contoh penggunaan **kwargs
def tampilkan_info(**data):
    for kunci, nilai in data.items():
        print(f"{kunci}: {nilai}")

# Pemanggilan fungsi
tampilkan_info(nama="Sutrisno", usia=30, pekerjaan="Programmer")

7. Kesimpulan

Fungsi dapat memiliki argumen untuk menerima data.

Argumen bisa memiliki nilai default.

Bisa menggunakan *args untuk menerima banyak nilai.

Bisa menggunakan **kwargs untuk menerima data dalam bentuk pasangan kunci-nilai.