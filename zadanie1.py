
x=int(input("Podaj rok urodzenia: "))
i=2021-x
min_val, max_val = 1830, 2021
if min_val <= x <= max_val:
    print(i)
    if i >= 18:
        print("Jestes pelnoletni!")
else:
    print ("Wprowadz normalnie")
