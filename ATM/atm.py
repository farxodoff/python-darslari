print("""----- ATM -----
1. Balansni Tekshirish
2. Pul Qo'shish
3. Pul Yechish
4. Chiqish""")
balans = 1000
while True:
    amal = int(input("Amalni kiriting: "))
    if(amal == 4):
        print("Yana kutib qolamiz!")
        break
    if(amal == 1):
        print(f"Balans {balans} so'm")
    elif(amal == 2):
        summa = float(input("Summa kiriting: "))
        balans += summa
        print(f"Yangi Balans: {balans} so'm")
    elif(amal == 3):
        summa = float(input("Summa kiriting: "))
        if(summa <= balans):
            balans -= summa
            print(f"Yangi Balans: {balans} so'm")
        else:
            print("Pul yetarli emas")
            continue