index = 1
endIndex = 10

while index <= endIndex:
    print(index)
    index += 1

#letter = ''
#while letter != 'x' and letter != 'X':
#    letter = input("Litera:")
#    print(letter)

letter = ''
while True:
    letter = input("Litera:")
    if letter == 'x' or letter == 'X':
        break
    else:
        print(letter)
