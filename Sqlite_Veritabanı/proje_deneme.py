import time

from kutuphane import *

print("""
****************************************

Kütüphane programımıza hoşgeldiniz

İşlemler:

1.Kitapları Göster

2.Kitap Sorgulama

3.Kitap ekle

4.Kitap sil 

5.Baskı Yükselt

Çıkmak için 'q' ya basın.

*****************************************
""")
kutuphane = Kutuphane()

while True:
    islem = input("Yapacağınız İşlem:")

    if(islem == "q"):
        print("Program sonlandırılıyor...")
        print("Yine bekleriz...")
        break
    elif(islem == "1"):
        kutuphane.kitaplari_goster()
    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz ?")
        print("Kitap sorgulanıyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)

    elif (islem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Tür:")
        baski = input("Baskı:")

        yeni_kitap= Kitap(isim,yazar,yayinevi,tur,baski)

        print("Kitap ekleniyor...")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi...")

    elif (islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?")

        cevap = input("Eminmisiniz?  (E/H)")

        if(cevap== "E"):
            print("Kitap Siliniyor....")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi...")

    elif (islem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baskı yükseltildi...")

    else:
        print("Geçersiz işlem")













