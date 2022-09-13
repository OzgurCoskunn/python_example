#Bu konuda bir diğer gömülü fonksiyonumuz olan reduce fonksiyonunu öğrenmeye çalışacağız.

#            reduce(function, iterasyon yapılabilen veritipi(liste vb.))

#reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular ve daha sonra çıkan sonucu
# listenin 3. elemanına uygular ve bu şekilde devam ederek liste bitince bir tane değer döner.

from functools import reduce  # reduce fonksiyonu son sürümlerde functools modülüne taşındı.

a = reduce(lambda x,y : x + y , [12,18,20,10])

print("listenin 1 ve 2 sini sonra 3,4,5.. olarak sırayla topluyor",a)

b = reduce(lambda x,y : x * y , [1,2,3,4,5])
print("listenin 1 ve 2 sini sonra 3,4,5.. olarak sırayla çarpıyor",b)

c = max([1,2,3,4,5,6])
print("maximumu buluyor :",c)

def maksimum(x,y):
    if (x > y):
        return x
    else:
        return y

d = reduce(maksimum, [-2,1,100,35,32])
print("reduce ile max fonksiyonu:",d)