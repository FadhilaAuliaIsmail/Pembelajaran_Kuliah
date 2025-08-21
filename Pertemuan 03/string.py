# String Normal
var1 = 'Hello Python'
var2 = "Programming with python"
print (var1)
print (var2)

print("===========================================================")
print("=+=+=+=+=+=+=+=+SubString+=+=+=+=+=+=+=+=")
# Dalam bahasa pemrograman Python, substring bisa didapatkan dengan menggunakan teknik yang disebut "pemotongan string" atau "slicing".
# Hanya saya tambah i supaya bisa jalan programnya.
vari1 = 'Hello Phyton'
vari2 = "I love Python"
print("vari1[0]", vari1[0])
print("vari2[2:6]", vari2[2:6])
print("===========================================================")

print("=+=+=+=+=+=+=+=+Immutable String+=+=+=+=+=+=+=+=")
# Mengubah nilai objek immutable, sebenarnya kita sedang membuat objek baru dengan nilai yang baru, bukan mengubah objek yang lama.
# Hanya saya hapus r supaya bisa jalan programnya.
va1 = 'Hello Phyton!'
va2 = va1 [:6]
print(va1)
print("String Update: - ", va1[:6] + 'World')
print("===========================================================")

print("=+=+=+=+=+=+=+=+Gabung String+=+=+=+=+=+=+=+=")
str1 = 'Hello'
str2 = 'Phyton'
# Kita bisa menggabungkan dua atau lebih string menjadi satu dengan menggunakan operator +.
# Menggunakan +.
print('str1 + str2 =', str1 + str2)
# Selain itu kita juga bisa melipatgandakan string menggunakan operator *.
# Menggunakan *.
print('str1 *3 =', str1 * 3)
print("===========================================================")

print("=+=+=+=+=+=+=+=+Contoh Hitung String+=+=+=+=+=+=+=+=")
# Untuk menghitung panjang dari string.
string = 'I love Phyton'
print(len(string))
print("===========================================================")

print("=+=+=+=+=+=+=+=+Karakter Escape String+=+=+=+=+=+=+=+=")
# Kita tidak bisa menggunakan tanda kutip tunggal maupun ganda.
# Menggunakan Kutip Tiga.
print ('''He said, "What's there?"''')
# Menggunakan karakter escape untuk tanda kutip tunggal.
print('He said, "What\'s there?"')
# Menggunakan karakter escape untuk tanda kutip ganda.
print("He said, \"What's there?\"")
# \n adalah newline (baris baru), jadi output-nya jadi dua baris:
print("Ini adalah baris pertama\nDan ini baris dua")
# \x48, \x45, dan \x58 adalah representasi hexadecimal atau /xHH ASCII: HEX atau
print("Ini adalah \x48\x45\x58")
# \x61 = ASCII Hex 61 → 'a' dan \n = newline (baris baru)
print("This is \x61 \nGood example")
# String diawali dengan r → semua escape sequence (\n, \x61, dll.) dianggap teks biasa, tidak diproses.
print(r"This is \x61 \nGood example")

print("===========================================================")

print("=+=+=+=+=+=+=+=+Format String+=+=+=+=+=+=+=+=")
# Memformat string dengan fungsi format() dibuat dengan menggunakan tanda {} sebagai placeholder atau posisi substring yang akan digantikan.
# Menggunakan posisi default
default_order = "{},{} dan {}".format("Budi","Galih","Ratna")
print('\n--- Urutan Default ---')
print(default_order)
# Menggunakan Argument posisi
positional_order = "{1},{0} dan {2}".format("Budi","Galih","Ratna")
print('\n--- Urutan berdasarkan posisi ---')
print(positional_order)
# Format Integer
print("{0} bila diubah jadi biner menjadi {0:b}".format (12))
# Format float
print("Format eksponensia: {0:e}".format(1566.345))
# Format Pembulatan
print("Sepertiga sama dengan: {0:.3f}".format(1/3))
# Format Rata
print("|{:<10}|{:^10}|{:>10}|".format('Beras','Gula','Garam'))
# String memiliki banyak fungsi bawaan.
print("Universitas Bina Sarana Informatika".lower())
print("Universitas Bina Sarana Informatika".upper())
print("I Love Programming in Python".split())
print("I Love Python".startswith("I"))
print("Saya belajar Python".endswith("on"))
print('-'.join(['I','love','you']))
print("Belajar Java di BSI".replace('Java','Python'))

nama = input("Masukkan nama Anda : ")
print("Hai " + nama + " Selamat bergabung di Bina Sarana Informatika")