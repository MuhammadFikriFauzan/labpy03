max = 0
while True:
	a = int (input("Masukkan bilangan: "))
	if a == 0:
		break
	if a > max:
		max = a
print ("Nilai terbesar adalah:",max)