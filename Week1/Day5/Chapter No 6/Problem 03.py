P1="Make a lot of money"
P2="buy now"
P3="subscribe this"
P4="click this"

message=input("Enter your text:  ")

if(P1 in message or P2 in message or P3 in message or P4 in message):
    print("This is Spam !")
else:
    print("This is not Spam !")