index = int(input("End number:"))

for value in range(0, index+1, 2):
    print(value, end=" ")
print("\n")
for number in range(index+1):
    if number % 2 == 0:
        print(number, "is even");
    else:
        print(number, "is odd");
