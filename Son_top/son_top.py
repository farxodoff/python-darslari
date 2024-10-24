from random import randint
import time

print("--- Son Top O'yini ---")

randson = randint(1,10)
tahmin_haqqi = 3

while True:
    tahmin = int(input("Tahminingiz[1-10]: "))
    while(tahmin < 0 or tahmin > 10):
        print("1-10 oralig'idagi son kiriting")
        tahmin = int(input("Tahminingiz[1-10]: "))
    if(tahmin < randson):
        print("LOADING!...")
        time.sleep(1)
        tahmin_haqqi -= 1
        print(f"Imkoniyat: {tahmin_haqqi}")
        print("Ozgina qo'shing Bratan!")
    elif(tahmin > randson):
        print("LOADING!...")
        time.sleep(1)
        tahmin_haqqi -= 1
        print(f"Imkoniyat: {tahmin_haqqi}")
        print("Sal qayting Bratan!")
    else:
        if(tahmin_haqqi == 3):
            print("Mashina sizniki!")
            break
        else:
            print("LOADING!...")
            time.sleep(1)
            print("Tabriklayman NIGGA!")
            break
    if(tahmin_haqqi == 0):
        print("Game Over NIGGA!")
        print(f"Aniq Javob: {randson}")
        break
