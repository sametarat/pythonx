a = []
x = input("Bir Cümle veya Kelime Gir : ")
x=x.lower()
a += x
b =[i for n , i in enumerate(a) if i not in a[:n]]
snc="".join(b)
print(snc)