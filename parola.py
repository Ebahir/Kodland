import random

harfler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Parlonanızın uzunluğunu giriniz."))
parola = ""

for i in range(uzunluk):
    sembol = random.choice(harfler)
    parola += sembol

print(parola)
