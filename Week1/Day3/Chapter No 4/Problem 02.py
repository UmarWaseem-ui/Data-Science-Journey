def f_to_c(f):
    c=5*(f-32)/9
    
f=int(input("Enter Temperature in F: "))
c=5*(f-32)/9
print(f"{round(c,2)}°C")