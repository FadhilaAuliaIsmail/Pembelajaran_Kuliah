print("Latihan 1")
# 1. Operator Penugasan (=, +=, -=, dll.)
x = 10      # assignment (penugasan)
x += 5      # sama dengan x = x + 5
print("Operator Penugasan:", x)   # Output: 15
# 2. Operator Logika (and, or, not)
a = True
b = False
print("Operator Logika:", a and b)  # Output: False
# 3. Operator Bitwise (&, |, ^, ~, <<, >>)
p = 6   # biner: 110
q = 3   # biner: 011
print("Operator Bitwise (p & q):", p & q)  # Output: 2 (biner 010)
# 4. Operator Identitas (is, is not)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("Operator Identitas:", list1 is list2)  # Output: False (beda objek di memori)
# 5. Operator Keanggotaan (in, not in)
nama = "Python"
print("Operator Keanggotaan:", "P" in nama)   # Output: True
print("=" * 40)

print("Latihan 2")
# ==========================================
# TOKO MAINAN ANAK
# ==========================================
print("=" * 40)
print("         TOKO MAINAN ANAK")
print("=" * 40)
# 1. Input data pembeli
nama_pembeli   = input("Masukan Nama Pembeli : ").strip()
kode_mainan    = input("Masukan Kode Mainan  : ").strip()
# 2. Input harga dan jumlah (dikonversi ke int)
while True:
    try:
        harga_satuan = int(input("Masukan Harga        : "))
        jumlah_beli  = int(input("Masukan Jumlah Beli  : "))
        if harga_satuan <= 0 or jumlah_beli <= 0:
            raise ValueError
        break
    except ValueError:
        print("  ⚠️  Harga & Jumlah harus berupa angka positif!\n")
# 3. Hitung total
total = harga_satuan * jumlah_beli
# 4. Cetak struk
print("=" * 40)
print(f"Nama Pembeli : {nama_pembeli}")
print(f"Kode Mainan  : {kode_mainan}")
print(f"Harga        : {harga_satuan:,}")
print(f"Jumlah Beli  : {jumlah_beli}")
print(f"TOTAL        : Rp {total:,}")