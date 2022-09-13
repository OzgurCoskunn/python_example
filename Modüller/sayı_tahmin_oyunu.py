import random
import time


print("""*********************************
SAYI TAHMİN OYUNU

1-40 arası sayı tahmin oyunu

*********************************
""")
rastgele_sayi = random.randint(1,40)
tahmin_hakki= 7


while True:
    tahmin = int(input("tahmininiz:"))

    if(tahmin < rastgele_sayi):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)

        print("daha yüksek bir sayı söyleyin")

        tahmin_hakki-= 1
    elif(tahmin > rastgele_sayi):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)

        print("daha düşük bir sayı söyleyin")

        tahmin_hakki -= 1
    else:
        print("bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Tebrikeler! Sayımız:", rastgele_sayi)
        break
    if(tahmin_hakki == 0):

        print("Tahmin kahhınız bitti")

        print("Sayımız:", rastgele_sayi)
        break


