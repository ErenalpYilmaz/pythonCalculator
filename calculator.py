#Basit bir hesap makinesi yapımı .
def topla(a, b):
    return a+b

def cikar(a, b):
    return a-b

def carp(a, b):
    return a*b

def bol(a,b):
    return a/b

sayi1 = float(input("1. sayıyı giriniz : "))
sayi2 = float(input("2. sayıyı giriniz : "))

islem = str(input("Yapmak istediğiniz işlemi seçiniz +-*/  :"))
sonuc = 0

match islem :
    case "+":
        sonuc = topla(sayi1,sayi2)
        print(f"Sonuc = {sonuc}")
    case "-":
        sonuc = cikar(sayi1,sayi2)
        print(f"Sonuc = {sonuc}")
    case "*":
        sonuc = carp(sayi1,sayi2)
        print(f"Sonuc = {sonuc}")
    case "/":
        sonuc = bol(sayi1,sayi2)
        print(f"Sonuc = {sonuc}")



