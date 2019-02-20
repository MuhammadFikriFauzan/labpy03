# labpy3

# **Latihan 1**

```python

import random

n=input("Masukan nilai N: ")


for x in range (1,6):
	print("Data ke:",x,"=>",random.uniform(0.0,0.5))
print("Selesai")
```
## Penjelasan algoritma

1. Masukan nilai N : 5.
2. Gunakan for range (untuk mengulang data dari 1-5).
3. Cetak data dan memasukan (random.uniform kurang dari 0.5).
4. Jika selesai RUN/jalankan programnya.

Output

![hasilnya](https://github.com/MuhammadFikriFauzan/labpy3/blob/master/1.png)

# **Latihan 2**
```python

max = 0
while True:
	a = int (input("Masukkan bilangan: "))
	if a == 0:
		break
	if a > max:
		max = a
print ("Nilai terbesar adalah:",max)
```
## Penjelasan algoritma
1. Masukan max=0

.
2. Gunakan while True (untuk perulangan tak terbatas. jika bilangan tersebut bukan nol ,maka akan terus berulang ).

3. Gunakan if (jika memasukan bilangan nol maka perulangan  akan berhenti).
4. Selanjutnya,gunakan if (untuk mencari nilai max = bilangan terbesar,lalu run/jalankan programnya).
Output

![hasilnya](https://github.com/MuhammadFikriFauzan/labpy3/blob/master/2.png)

# **Program 1**
```python
a=100000000
for x in range(1,9):
	if(x>=1 and x<=2):
		b = a*0
		print("Laba Bulan ke-",x,":",b)
	if(x>=3 and x<=4):
		c = a*0.1
		print("Laba Bulan ke-",x,":",c)
	if(x>=5 and x<=7):
		d = a*0.5
		print("Laba Bulan ke-",x,":",d)
	if(x==8):
		e = a*0.2
		print("Laba Bulan ke-",x,":",e)
total = b+b+c+c+d+d+d+e
print("\ntotal : ", total)
```
## Penjelasan algoritma
1. Masukkan nilai a.

2. Gunakan for untuk perulangan dari 1 sampai 8

.
3. Lalu gunakan if pertama untuk menentukan laba bulan ke 1 dan ke 2, masukan variabel (b) kalikan nilai (a) dengan data bulan 1 dan 2, 
cetak (x) dan (b).

4. Lalu gunakan if kedua untuk menentukan laba bulan ke 3 dan ke 4, masukan variabel (b) kalikan nilai (a) dengan data bulan 3 dan 4, 
cetak (x) dan (c).
5. Lalu gunakan if ketiga untuk menentukan laba bulan ke 5 sampai ke 7, masukan variabel (b) kalikan nilai (a) dengan data bulan 5 sampai 7, cetak (x) dan (d)
.
6. Lalu gunakan if keempat untuk menentukan laba bulan ke 8, masukan variabel (b) kalikan nilai (a) dengan data bulan 8, 
cetak (x) dan (e).

7. Lalu total keseluruhan.


8. Cetak total
.
Output

![hasilnya](https://github.com/MuhammadFikriFauzan/labpy3/blob/master/3.png)
