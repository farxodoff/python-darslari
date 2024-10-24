import time

db_user = "admin"
db_password = "123"
imkoniyat = 3

while True:
    if(imkoniyat > 0):
        user = input("Username: ")
        password = input("Password: ")
        if(db_user != user and db_password != password):
            print("Username va Password xato kiritildi")
            imkoniyat -= 1
            print(f"Imkoniyat = {imkoniyat}")
        elif(db_user != user and db_password == password):
            print("Username xato kiritildi")
            imkoniyat -= 1
            print(f"Imkoniyat = {imkoniyat}")
        elif(db_user == user and db_password != password):
            print("Password xato kiritildi")
            imkoniyat -= 1
            print(f"Imkoniyat = {imkoniyat}")
        elif(db_user == user and db_password == password):
            print("Tizimga Xush Kelibsiz!")
            break
    else:
        print("10 soniyadan keyin qayta urunib ko'ring!")
        for i in range(10,0,-1):
            time.sleep(1)
            print(f"{i} soniya")
        imkoniyat = 3

