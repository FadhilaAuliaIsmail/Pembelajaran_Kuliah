import decimal
import fractions
import math

print("Bilangan Decimal")
a = 12.3456789
# %f → format angka float (bilangan desimal).
# %.2f → tampilkan 2 angka di belakang koma.
print('Nilai a = %3.2f' %a)
# %.4f → tampilkan 4 angka di belakang koma.
print('Nilai a = %3.4f' %a)

# Fungsi int() akan mengkonversi float ke integer dengan membuang bagian desimalnya (bukan pembulatan).
print(int(2.5))
# Sama, 3.8 → buang desimal → 3
print(int(3.8))
# Fungsi float() mengubah bilangan bulat menjadi floating point (ada koma).
print(float(5))

# Komputer menyimpan angka pecahan dalam format biner floating point.
print(1.1 + 2.2)
# Karena 3.3000000000000003 ≠ 3.3, maka hasilnya False.
print((1.1 + 2.2) == 3.3)

# Output: 0.1
print(0.1)
# Output: Decimal 0.1000000000000000055511151231257827021181583404541015625
print(decimal.Decimal(0.1))

# Output: 3/2
print(fractions.Fraction(1.5))
# Output: 1/3
print(fractions.Fraction(1,3))

from fractions import Fraction as F
# Output: 2/3
print(F(1,3) + F(1,3))
# Output: 6/5
print(1 / F(5,6))
# Output True
print(F(-3,10)<0)

# Output: 3.141592653589793
print(math.pi)
# Output: -1.0
print(math.cos(math.pi))
# Output:
print(math.exp(5))
# Output: 2.0
print(math.log10(100))
# Output: 120
print(math.factorial(5))