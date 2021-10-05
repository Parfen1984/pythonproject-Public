set1 = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048}
set2 = {1, 4, 16, 64, 256, 1024, 4096, 16384}
# set1.add(4096)
# print(set1)
# val1 = int(input("Podaj liczbę:"))
# if val1 in set1:
#     print(val1, "jest potegą liczby 2")
# if val1 in set2:
#     print(val1, "jest potegą liczby 4")
# list1 = [1, 3, 9, 3, 99, 12, 4, 3, 1]
# print(list1)
# set3 = set(list1)
# print(set3)

print("Suma", set1.union(set2))
listUnion = list(set1 | set2)
listUnion.sort()
print(listUnion)
print("Iloczyn", set1.intersection(set2))
print(sorted(set1 & set2))
print("Różnica 1:", set1.difference(set2))
print("Różnica 2:", set2.difference(set1))
