fib = []
n = int(input("Długość ciągu Fibonacciego:"))

for index in range(n):
    if index == 0 or index == 1:
        fib.append(index)
    else:
        fib.append(fib[-1]+fib[-2])

print(fib)
