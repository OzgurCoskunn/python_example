

print("""*********************************************
Faktoriyel bulma programı

Çıkmak için 'q' ya basınız...

*********************************************""")

while True:
    sayi = input("sayı:")
    if(sayi == "q"):
        print("program sonlandırılıyor...")
        break

    else:
        sayi = int(sayi)

    faktoriyel = 1

    for i in range(2,sayi+1):
        print("Faktoriyel",faktoriyel,"i:",i)
        faktoriyel *= i
    print("Faktoriyel",faktoriyel)


