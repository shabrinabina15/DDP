#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0

print('---mencari celcius ke fahrenheit----')
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit
print("jadi suhu yang dikonversi ke Fahrenheit", celcius_ke_fahrenheit(0))
print("jadi suhu yang dikonversi ke Fahrenheit", celcius_ke_fahrenheit(100))


#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))  # Output: True
#print(is_genap(7))  # Output: False

print()
print('----mencari bilangan genap----')
def is_genap(bilangan_genap):
    return bilangan_genap %2 == 0
# untuk memasukkan value
print(is_genap(4), "karena bilangan bernilai genap")
print(is_genap(7), "karena bilangan bernilai ganjil")


#Buatlah fungsi untuk melihat keterangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai(60) #gagal

print()
print('----mencetak nilai kelulusan----')
#rata-rata nilai 70
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return 'lulus'
    else :
        return 'gagal'

# untuk mencetak value
print(nilai_kelulusan(80), "karena nilai kelulusannya 80")
print(nilai_kelulusan(60), "karena nilai kelulusannya 60")

#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,5,7,9,11,13,15,17,19

print()
print('----mencetak bilangan ganjil----')
def bilangan_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end=" ")
# untuk memasukkan value
print(bilangan_ganjil(20))