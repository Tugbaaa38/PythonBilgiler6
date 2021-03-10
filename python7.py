# if/else if/elif bir ornegi bir kac farkli sekilde cozelim....


print("*****************************************************************************\n")
system_mail="bilgi38@gmail.com"
system_password="12345TK"

kullanici_mail=input("Mail adresinizi girin:")
kullanici_password=input("Sifrenizi girin:")

basariliMi=(system_mail==kullanici_mail) and (system_password==kullanici_password)
#burada ise true veya false bir deger alacagız ve basariliMi adli degiskene atayacagiz.
if basariliMi==True:
    print("GIRIS BASARILI!")
else:
    print("GIRIS BASARISIZ!")
print("*****************************************************************************\n")

print("*****************************************************************************\n")
mail="bilgi38@gmail.com"
password="12345TK"

girilen_mail=input("Mail adresinizi girin:")
girilen_password=input("Sifrenizi girin:")

if(mail==girilen_mail and password==girilen_password):
    print("Giris Basarili!")
elif(mail!=girilen_mail or password!=girilen_password):
    print("Kullanici adi veya sifre hatali!")
print("*****************************************************************************\n")

print("*****************************************************************************\n")
kullanici_adi=input("Kullanici adi girin:")
parola=input("Parolanizi girin:")
#Burada dikkat edecek olursaniz parolayı string turunde aldik.Cunku uzunluk bulmamiz gerek.

adUzunluk=len(kullanici_adi)
parolaUzunluk=len(parola)       

if adUzunluk<8 or adUzunluk>10 or parolaUzunluk<8 or parolaUzunluk>10:
    print("Kullanici adi ve parola 8 haneden kisa ve 10 haneden uzun olmamalidir..")
else:
    print("SISTEME HOS GELDINIZ!")
print("*****************************************************************************\n")

print("*****************************************************************************\n")
kullanici_adi=input("Kullanici adi girin:")
parola=input("Parolanizi girin:")

adUzunluk=len(kullanici_adi)
parolaUzunluk=len(parola)       

if adUzunluk<8 or adUzunluk>10:
    print("Kullanici adi 8 haneden kisa ve 10 haneden uzun olmamalidir..")
else:
    if parolaUzunluk<8 or parolaUzunluk>10:
        print("Parola 8 haneden kisa ve 10 haneden uzun olmamalidir..")
    else:
        print(f"SİSTEME HOS GELDİNİZ {kullanici_adi}")
print("*****************************************************************************\n")