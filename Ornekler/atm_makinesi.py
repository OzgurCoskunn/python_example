

print("""****************************************************
ATM Makinesine Hoşgeldiniz

İşlemler;

1. Bakiye sorgulama
2. Para yatırma
3. Para çekme

Programdan çıkmak için 'q' ya basınız...
**************************************************

""")
bakiye = 1000

while True:
    islem = input("işlemi seçiniz:")

    if(islem == "q"):
        print("yine bekleriz")
        break
    elif(islem == "1"):
        print("bakiyeniz {} tl dir".format(bakiye))

    elif(islem == "2"):
        miktar = int(input("Miktarı giriniz"))

        bakiye+=miktar

    elif(islem == "3"):
        miktar = int(input("Miktarı giriniz"))

        if(bakiye - miktar<0):
            print("bölye bir miktar çekemezsiniz")
            continue

        bakiye-=miktar

    else:
        print("Geçersiz işlem...")





















