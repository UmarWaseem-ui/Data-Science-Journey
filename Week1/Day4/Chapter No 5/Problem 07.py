# Student Marks list
student=[   
    {"name": "Umar", "marks": 90,},
    {"name": "Ahmad", "marks": 70,},
    {"name": "Ali", "marks": 80}
]

for student in student:
    print(f"{student['name']}: {student['marks']}")

# To-Do list
L=[
    {"Day":"Monday", "To-DO": "CLeaning"},
    {"Day":"Tuesday", "To-DO": "Shoping"},
    {"Day":"Wednesday", "To-DO": "Movie"},
    {"Day":"Thursday", "To-DO": "Outing"}
]
print(f"{L[0]['Day']}: {L[0]['To-DO']}")

# Storing Student Data
Students=[]
Name=input("Enter the name of student: ")
Students.append(Name)
Name=input("Enter the name of student: ")
Students.append(Name)
Name=input("Enter the name of student: ")
Students.append(Name)
Name=input("Enter the name of student: ")
Students.append(Name)

print(Students)