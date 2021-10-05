import random
randomNumber = random.randrange(0, 100)

while True:
    myNumber = int(input("Liczba całkowita z przedziału od 0 do 100:"))
    if myNumber == randomNumber:
        print("Brawo! Wylosowana liczba to", randomNumber)
        break
    elif myNumber < randomNumber:
        print('Wylosowana liczba jest większa.')
    else:
        print('Wylosowana liczba jest mniejsza.')
