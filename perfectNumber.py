# Perfect Number
number = int(input("Son kiritng: "))
sum = 0
for i in range(1, number):
    if(number % i == 0):
        sum = sum + i
if (sum == number):
    print("Perfect Son!")
else:
    print("Perfect Son emas")
