# Contoh penggunaan **kwargs
def tampilkan_info(**data):
    for kunci, nilai in data.items():
        print(f"{kunci}: {nilai}")

# Pemanggilan fungsi
tampilkan_info(nama="Sutrisno", pekerjaan="Programmer",alamat="Bogor")