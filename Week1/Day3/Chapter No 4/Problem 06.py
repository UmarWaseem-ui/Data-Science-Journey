def table(n):
    for i in range(1,11):
     print(f"{n} x {i} = {n*i}")
    i=1
    n=n*i
    return n

n=int(input("Enter the Number: "))
table(n)