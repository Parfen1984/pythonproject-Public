def print10(str):
    for i in range(1, 11):
        print(i, str)

#print10("Czerwiec")

def divNumber(a, b):
    if b == 0:
        return False;
    else:
        return a/b;

print(divNumber(80,0))
