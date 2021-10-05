def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

userValue = int(input("Podaj liczbę: "))
if isPrime(userValue):
    print(userValue, "to liczba pierwsza")
else:
    print(userValue, "nie jest liczbą pierwszą")
