import math
t = int(input("Program kac defa calısacak : "))
if t <=0:
    print("Döngü sıfırdan küçük olamaz")
for i in range(0,t):
    sayi1 = int(input("Birinci Sayıyı Giriniz: "))
    sayi2 = int(input("İkinci Sayıyı Giriniz: "))
    islem = input("Yapılmasını İstediğiniz İşlemi Giriniz: ")

    if islem == "+":
        print(sayi1+sayi2)
    elif islem == "-":
        print(sayi1-sayi2)
    elif islem == "*":
        print(sayi1*sayi2)
    elif sayi2 == 0:
        print("Bir sayıyı sıfıra bölemezsiniz")
    elif islem == "/":
        print(sayi1/sayi2)
    elif islem == "cık":
        break
    else:
        print("Lütfen + - / * isaretlerinden  birini giriniz.")