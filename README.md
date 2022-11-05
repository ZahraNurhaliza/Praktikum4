# Praktikum4

## Labspy02
### Flowchart menentukan bilangan terbesar dari 3 buah bilangan
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/Flowchart%20praktikum2.png)

### Algoritma
1. Start
2. Masukan nilai a,b,c
3. Melakukan proses untuk menentukan bilangan mana yang memiliki bilangan terbesar dengan steatment if
4. Melakukan pencetakan hasil proses
5. End

### Programan menentukan bilangan terbesar dari 3 buah bilangan
Rumus
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/praktikum2.png)

Setelah di run
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/praktikum2(1).png)

## Labpy03

### Latihan1
#### Flowchart latihan1
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/Flowchart%20latihan1.png)

#### Algoritma latihan1
1. Start
2. Masukan fungsi random terlebih dahulu
3. Deklarasi interger
4. Masukan nilai jumlah N
5. Mencetak data ke 1 sampai 5 dengan hasil nilai kurang dari 0,5
6. End

#### Program latihan1
Rumus
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/latihan1.py.png)

Setelah di run
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/latihan1.py(1).png)

### Latihan2
#### Flowchart latihan2
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/Flowchart%20latihan2.png)

#### Algoritma latihan2
1. Start
2. Interger max = 0
3. Menggunakan fungsi perulangan while true, hingga menampilkan perulangan sampai batas tertentu
4. Memasukan bilangan integer pada "a"
5. Menggunakan fungsi if jika max kurang dari nilai a, maka max sama dengan a
6. Mengunakan fungsi if jika nilai a adalah 0 maka fungsi break artinya perulangan berhenti jika menulis nilai 0
7. Mencetak nilai paling terbesarv setelah break, sehingga menampilkan nilai terbesar diantara bilangan tersebut dalam perulangan
8. End

#### Program latihan2
Rumus
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/latihan2.py.png)

Setelah di run
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/latihan2.py(1).png)

## Program1 (Praktikum3)
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan
modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada
bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5,
pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan
keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8
bulan berjalan usahanya.

#### Algoritma program1
1. Start
2. Mula -mula masukkan modal usahanya yaitu a = 100000000
3. Gunakan perintah for m in range (1,9):, for ini untuk perulangan dari 1 sampai 8, kenapa menggunakan for,karena for ini perulangan yang terhitung. Pada skirp in range(1, 9) akan mebentuk list perulangan yang berisi [1,2,3,4,5,6,7,8] nah dan bahwa iterasi 9 itu tidak termasuk, untuk membuktikan bawa perulangan ini hanya sampai 8 saja
4. Lalu gunakan perintah _if(m>=1 and m<=2): b=a*0. if pertama ini untuk menentukan laba bulan ke 1 dan ke 2.masukan variable kalikan nilai (a) dengan data bulan 1 dan 2. lalu print("Laba bulan ke-",m," :",b) untuk menampilkan hasil laba. pada bulan pertama dan kedua belum mendapatkan laba jadinya 0
5. if(m>=3 and m<=4): c=a*0.1. if yang kedua ini untuk menentukkan laba bulan ke 3 dan ke 4.masukan variable kalikan nilai (a) dengan data bulan 3 dan 4. pada bulan ke 3 itu baru mendapatkan laba sebesar 1% berarti bulan ke 4 juga sama. lalu cetak (m) dan (c), dengan perintah print("Laba bulan ke-",m," :",c)
6. if(m>5 and m<=7): d=a*0.5.if ketiga untuk menentukan laba bulan ke 5 sampai ke 7.masukan variable lalu kalikan nilai (a) dengan data bulan 5 sampai 7, pada bulan ke 5 laba naik sebesar 5% berarti pada bulan ke 6 dan 7 kenaikan labanya sama, lalu cetak (m) dan (d), dengan perintah print ("Laba bulan ke-",m," :",d)
7. if(m==8): e=a*0.2 if keempat atau yang terakhir ini untuk menentukan laba bulan ke 8. lalu masukan variabel kalikan nilai (a) dengan data bulan 8. Pada laba bulan ke 8 ini menurun sebanyak 2%, lalu cetak (m) dan (e) dengan perintah_ print ("Laba bulan ke-",m," :",e)
8. Kemudian yang terakhir totalkan keseluruhan laba yaitu total = b+b+c+c+d+d+d+e
9. lalu print("Total laba adalah : ", total), untuk menampilkan hasil keseluruhan laba dari bulan pertama sampai bulan kedelapan
10. End

#### Program program1
Rumus
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/program1.py.png)

Setelah di run
![image](https://github.com/ZahraNurhaliza/Praktikum4/blob/main/screenshot/program1.py(1).png)

Setelah selesai commit dan push ke repository github
