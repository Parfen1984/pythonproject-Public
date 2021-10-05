for i in range(1, 101, 1):
    print (i)
    if i % 3 == 0:
        print(f" {i} Good")
    elif i % 5 == 0:
        print(f" {i} BETTER ")
    if i % 3 ==0 and i % 5 == 0:
        print(f" {i} Best ")
