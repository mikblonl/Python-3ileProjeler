#Muhammed İkbal Önal
#Python Basit Düzey Hesap Makinesi / Python Simple Calculator

işlemler = """
(1) Topla
(2) Çıkar
(3) Çarp
(4) Böl
"""

print(işlemler) 

soru = input("Yapmak istediğiniz işlemin numarasını giriniz: ")

if soru == "1":
    sayı1 = int(input("Toplama işlemi için ilk sayıyı giriniz :"))
    sayı2 = int(input("Toplama işlemi için ikinci sayıyı giriniz :"))
    print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

elif soru == "2":
    sayı3 = int(input("Çıkarma işlemi için ilk sayıyı giriniz: "))
    sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz: "))
    print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

elif soru == "3":
    sayı5 = int(input("Çarpma işlemi için ilk sayıyı giriniz: "))
    sayı6 = int(input("Çarpma işlemi için ikinci sayıyı giriniz: "))
    print(sayı5, "x", sayı6, "=", sayı5 * sayı6)
   

elif soru == "4":
    sayı7 = int(input("Bölme işlemi için ilk sayıyı giriniz: "))
    sayı8 = int(input("Bölme işlemi için ikinci sayıyı giriniz: "))
    print(sayı7, "/", sayı8, "=", sayı7 / sayı8)
    

else:
    print("Bu işlemi gerçekleştiremezsiniz! ")
    print("Lütfen geçerli bir işaret giriniz! ", işlemler)

