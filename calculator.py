#Basit bir hesap makinesi yapımı .
def topla(a, b):
    return a+b

def cikar(a, b):
    return a-b

def carp(a, b):
    return a*b

def bol(a,b):
    return a/b

def islem(islem):
    sonuc = 0
    match islem:
        case "+":
            sonuc = topla(sayi1, sayi2)
            print(f"Sonuc = {sonuc}")
        case "-":
            sonuc = cikar(sayi1, sayi2)
            print(f"Sonuc = {sonuc}")
        case "*":
            sonuc = carp(sayi1, sayi2)
            print(f"Sonuc = {sonuc}")
        case "/":
            sonuc = bol(sayi1, sayi2)
            print(f"Sonuc = {sonuc}")

def tekrar(islemStr):
    tekrarSayisi = 0
    sonuc = ""
    for i in "+-*/":
        if islemStr == i:
            tekrarSayisi +=1
            sonuc +=""
    if tekrarSayisi ==1 :
        islem(islemStr)
    else :
        print("Yapmak istediğiniz işlemi yanlış belirttiniz . ")


try :
    sayi1 = float(input("1. sayıyı giriniz : "))
    sayi2 = float(input("2. sayıyı giriniz : "))
    islemStr = str(input("Yapmak istediğiniz işlemi seçiniz +-*/  :"))
    tekrar(islemStr)
except :
    print("Hatalı işlem yaptınız.")














