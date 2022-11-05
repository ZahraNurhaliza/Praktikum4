# Perulangan Latihan 1
# Menggunakan For

print("Menampilkan bilangan acak yang lebih kecil dari 0.5")
import random

jumlah = int(input("Masukkan nilai N : "))
a = 0

for i in range(jumlah):
    a +=1
    b = random.uniform(.0,.5)
    print("Data ke:",a,"==>",b)

print("Selesai")