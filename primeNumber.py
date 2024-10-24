num = int(input("Son kiriting: "))
if num > 1:
    for i in range(2, (num // 2) + 1):
        if (num % i) == 0:
            print(num, "Tub Son emas")
            break
    else:
        print(num, "Tub Son")
else:
    print(num, "Tub Son emas")
