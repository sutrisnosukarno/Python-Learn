# Contoh penggunaan *args
def nilai(*angka):
    return max(angka)

# Pemanggilan fungsi
print(nilai(1, 2, 3, 4, 5, 5, 10, 20))