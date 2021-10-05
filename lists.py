myList = [25, "kwiecień", 2021, "Narzędzia ...", "Struktury danych w języku Python"]

#print(myList[0]) #pierwszy element
#print(myList[-1]) #ostatni element

myList[3] = "Przedmiot: Narzędzia procesu tworzenia oprogramowania"
#print(myList[-2])
myList[-1] = "Temat: " + myList[-1]
#print(myList[4])

myList.insert(3, "8:15 - 10:15")
myList.append("https://github.com/WebCampPL/PythonWSE2021.git")

print(myList)

#for value in myList:
#    print("->", value)

for index, value in enumerate(myList):
    print(index, "-", value)

#myList.remove(2021)
#myList.pop(-1)
#print(len(myList), myList)
