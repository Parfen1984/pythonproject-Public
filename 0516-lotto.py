print('Losowanie DUŻEGO LOTKA')
wybrane = [17, 22, 41, 35, 19, 37]
for i in range(1, 7):
    print("Liczba ", i)
    wybrane.append(int(input()))
print("Zaznaczone liczby: ", wybrane)

import random
wylosowane = random.sample(range(1, 50), 6)
print("Wylosowane liczby: ", wylosowane)

trafione = set(wybrane) & set(wylosowane)
print("Trafiłeś", len(trafione))
print("Trafione liczby to:", trafione)
