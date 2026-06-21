A1=int(input("Enter your English Marks: "))
A2=int(input("Enter your Maths Marks: "))
A3=int(input("Enter your Computer Marks: "))

subject_percentage=(100*(A1))/100

if(subject_percentage>=33):
    print("You passed the Subject English !!!", subject_percentage,"%")

else:
    print("You Failed !!!", subject_percentage,"%")


subject_percentage=(100*(A2))/100

if(subject_percentage>=33):
    print("You Passed the Subject Maths !!!", subject_percentage,"%")

else:
    print("You Failed !!!", subject_percentage,"%")


subject_percentage=(100*(A3))/100

if(subject_percentage>=33):
    print("You Passed the Subject Computer !!!", subject_percentage,"%")

else:
    print("You Failed !!!", subject_percentage,"%")

total_percentage=(100*(A1+A2+A3))/300

if(total_percentage>=40):
    print("You have Passed the Exam !!!", total_percentage,"%")

else:
    print("You Failed the Exam !!!", total_percentage,"%")
 