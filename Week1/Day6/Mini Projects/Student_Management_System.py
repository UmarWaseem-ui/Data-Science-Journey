# Features:
    # Add student
    # Show student list
    # Search student

def Students(count=5):
    students = []
    for i in range(count):
        name = input(f"Enter the name of student {i+1}: ")
        students.append(name)
    return students

student_list = Students()

print("\nStudent List:", student_list)

print("2nd Student is:", student_list[1])