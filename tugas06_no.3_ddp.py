#Tugas
#● Buat program untuk minta input jumlah baris dan buat rangkaian berikut ini
#*
#**
#***
#****
#● Dan seterusnya sejumlah baris yang diinputkan
#● Gunakan for loop dengan range
s = int(input("Masukan jumlah baris : "))
for m in range(1, s+1) :
    print("*" * m)