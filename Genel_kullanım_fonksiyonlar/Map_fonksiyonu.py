# Pythonda gömülü bir fonksiyon olan map() fonksiyonunun yapısı şu şekildedir.
#
#                 map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)
#
# map() fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır. (Fonksiyonlar da birer obje olduğu için başka bir fonksiyona gönderilebilir.)
# 2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak ,
# gönderilen fonksiyonu her bir eleman üzerinde uygulayarak sonuçları bir map objesi olarak döner.

def double(x):
    return x * 2


s =list(map(double,[1,2,3,4,5,6,7]))
print("fonksiyonla birer birer listeyi kullanıp çarpıyor:",s)

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

b = list(map(lambda x,y : x * y , liste1,liste2))

a = list(map(lambda x,y,z : x * y * z , liste1,liste2,liste3))
print("ikili liste :",b)
print("üçlü liste :",a)



