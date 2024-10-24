num = int(input("Son kiriting: "))
sum = 0
temp = num

while (temp>0):
    sum = sum + ( (temp%10)**3 )
    temp = temp // 10

if sum == num:
    print("Armstrong Son")
else:
    print("Armstrong Son emas")