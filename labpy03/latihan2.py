# Menetukan Bilangan Terbesar

max = 0 # Menetukan bilangan terbesar
while True :
    a = int(input("Masukkan bilangan = "))
    if max < a:
        max = a
    if a== 0:
        break # Mengakhiri perulangan

print("Bilangan terbesar adalah: ",max)