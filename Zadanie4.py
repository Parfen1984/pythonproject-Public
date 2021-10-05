def silnia(n):
    if n==0:
        return 1
    elif n>0:
         return n*silnia(n-1)
    else:
        return False
data = []
with open('data.txt', 'r') as f:
    for line in f:
        num = int(line)
        print(num)

print("silnia(",num,") = ", silnia(num))
