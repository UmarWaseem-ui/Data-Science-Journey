def Greatest(a,b,c):
    if(a>b and a<c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>a and c>b):
        return c

a=2
b=4
c=6

print(Greatest(a,b,c))