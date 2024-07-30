#Basit bir hesap makinesi yapımı .
def topla(a, b):
    return a+b

def cikar(a, b):
    return a-b

def carp(a, b):
    return a*b

def bol(a,b):
    return a/b

def islem(islem,sayi1,sayi2):

    if islem not in "+-?*":
        return "Lutfen su islemlerden birini seciniz :+-?*"

    match islem:
        case "+":
            sonuc = topla(sayi1, sayi2)
            return f"Sonuc = {sonuc}"
        case "-":
            sonuc = cikar(sayi1, sayi2)
            return f"Sonuc = {sonuc}"
        case "*":
            sonuc = carp(sayi1, sayi2)
            return f"Sonuc = {sonuc}"
        case "/":
            sonuc = bol(sayi1, sayi2)
            return f"Sonuc = {sonuc}"

while True:
    try:
        sayi1 = float(input("1. sayıyı giriniz : "))
        sayi2 = float(input("2. sayıyı giriniz : "))
        islemStr = str(input("Yapmak istediğiniz işlemi seçiniz +-*/  :"))
        print(islem(islemStr,sayi1,sayi2))
    except:
        print("Lutfen sayilari duzgun giriniz.")















