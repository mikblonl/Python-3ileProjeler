#Muhammed İkbal Önal - mikblonl
#Python Orta Düzey Hesap Makinesi / Python Intermediate Calculator
giriş = """                        
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) küpünü hesapla
    (7) karakökünü hesapla
    (8) logaritmasını hesapla
    (9) faktoriyelini hesapla
    (10) yukarı yuvarla
    (11) aşağı yuvarla
    (12) mutlak değer alma
    (13) cosinus hesapla
    (14) sinus hesapla
    (15) tanjant hesapla
    """
print(giriş)

import math #matematik fonksiyonlarını kullanabilmek için  içe aktarıyoruz.
import time #zaman fonksiyonlarını kullanabilmek için  içe aktaryoruz.

a = 1

while a == 1:
    soru = input("Yapmak istediğiniz işlemin numarasını giriniz... (Çıkmak için q): ")

    if soru == "q":
        print("Çıkılıyor...")
        time.sleep(3)
        a = 0

    elif soru == "1":
        sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
        sayı2 = int(input("toplama işlemi için ikinci sayıyı girin: "))
        print("%s + %s = %s" %(sayı1, sayı2, sayı1 + sayı2))

    elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print("%s - %s = %s" %(sayı3, sayı4, sayı3 - sayı4))

    elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
        print("%s x %s = %s" %(sayı5, sayı6, sayı5 * sayı6))

    elif soru == "4":
        sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
        sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
        print("%s / %s = %s" %(sayı7, sayı8, sayı7 / sayı8))

    elif soru == "5":
        sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
        print("%s sayısının karesi = %s" %s(sayı9, sayı9 ** 2))

    elif soru == "6":
        sayı10 = int(input("Küpünü hesaplamak istediğiniz sayıyı girin: "))
        print("%s sayısının küpü = %s" %(sayı10, sayı10 ** 3))

    elif soru == "7":
        sayı11 = int(input("Karakökünü hesaplamak istediğiniz sayıyı girin: ")) 
        print("%s sayısının karakökü = %s" %(sayı11, sayı11 ** 0.5))


    elif soru == "8":
        sayı12 = int(input("Logaritmasını hesaplamak istediğiniz sayıyı girin: "))
        print("%s sayısının logaritması = %s" %(sayı12, math.log(sayı12)))

    elif soru == "9":
        sayı13 = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı girin: "))
        print("%s sayısının faktoriyeli = %s" %(sayı13, math.factorial(sayı13)))

    elif soru == "10":
        sayı14 = float(input("Yukarı yuvarlamak istediğiniz sayıyı giriniz: "))
        print("%s sayısının yuvarlaması = %s" %(sayı14, math.ceil(sayı14)))

    elif soru == "11":
        sayı15 = float(input("Aşağı yuvarlamak istediğiniz sayıyı giriniz: "))
        print("%s sayısının yuvarlaması = %s" %(sayı15, math.floor(sayı15)))

    elif soru == "12":
        sayı16 = int(input("Mutlak değerini almak istediğiniz sayıyı girin: "))
        print("%s sayısının mutlak değeri = %s" %(sayı16, math.fabs(sayı16)))

    elif soru == "13":
        sayı17 = int(input("Cosinus'unu bulmak istediğiniz sayıyı girin: "))
        print("%s sayısının radyan cinsinden cosinusu = %s" %(sayı17, math.cos(sayı17)))

    elif soru == "14":
        sayı18 = int(input("Sinusunu bulmak istediğiniz sayıyı girin: "))
        print("%s sayısının radyan cinsinden sinusu = %s" %(sayı18, math.sin(sayı18)))

    elif soru == "15":
        sayı19 = int(input("Tanjantını bulmak istediğiniz sayıyı girin: "))
        print("%s sayısının radyan cinsinden tanjantı = %s" %(sayı19, math.tan(sayı19)))

    else:
        print("Yanlış giriş!")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)

    

        
