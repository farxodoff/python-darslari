def factorialWhile(number):
    f = 1
    if(number == 0 or number == 1):
        print(f"Factorial = {f}")
    else:
        while(number > 1):
            f *= number
            number -= 1
        print(f"Factorial = {f}")

factorialWhile(int(input("Enter in number: ")))

# -- / -- / -- / -- / -- / -- / -- / -- / -- / -- / -- / -- / --

def factorialFor(number):
    f = 1
    if (number == 0 or number == 1):
        print(f"Factorial = {f}")
    else:
        for i in range(1, number+1):
            f *= i
        print(f"Factorial = {f}")

factorialFor(int(input("Enter in number: ")))
