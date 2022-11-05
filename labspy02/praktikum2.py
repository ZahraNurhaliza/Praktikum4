# Menggunakan steatment if

def pengulangan():
    print("Program menentukan bilangan terbesar dari 3 bilangan")
    a = int(input ("Masukan nilai ke-1 = "))
    b = int(input ("Masukan nilai ke-2 = "))
    c = int(input ("Masukan nilai ke-3 = "))

    if a>b and a>c:
        print("Nilai terbesar :", a)
    elif b>a and b>c:
        print("Masukan terbesar :", b)
    else:
        print("Masukan terbesar :", c)

    print('')
    print('ingin coba lagi? (ya/tidak)')
    x = input()
    if x == 'ya':
        return pengulangan()
    if x == 'tidak':
        print('selesai.')

pengulangan()