kelime = input("Bir Kelime Gir : ")
a = int(input("Başlangıç Sayısı Gir : "))
b = int(input("Bitiş Sayısını Gir : "))
if a > len(kelime) or b > len(kelime):
    print("Kelimeden Büyük Değer Giremezsiniz!")
else:
    if a <= 0 or b <= 0:
        print("Sıfır Değeri Giremezsiniz")
    else:
        a = a-1
        print("Girilen Kelime : ", kelime)
        print("Kesilen Kelime : {}".format(kelime[:a]+kelime[b:]))