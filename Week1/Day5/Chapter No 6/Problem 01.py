A1=int(input("Enter the Number: "))
A2=int(input("Enter the Number: "))
A3=int(input("Enter the Number: "))
A4=int(input("Enter the Number: "))

if(A1>A2 and A1>A3 and A1>A4):
    print(A1, "is the largest number")

elif(A2>A1 and A2>A3 and A2>A4):
    print(A2, "is the largest number")

elif(A3>A1 and A3>A2 and A3>A4):
    print(A3, "is the largest number")

else:
    print(A4, "is the largest number")