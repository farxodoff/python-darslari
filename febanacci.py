def febanacci(number):
    b = 1
    a = 0
    c = 0
    for i in range(1, number+1):
        c = a + b
        a = b
        b = c
    print(c)

febanacci(int(input("Son kiriting: ")))