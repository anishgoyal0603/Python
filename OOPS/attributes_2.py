class Student:
    PI = 3.1

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        self.PI = 3.14

stu1 = Student("Rahul",9.2)

print(stu1.name)
print(stu1.PI) # 3.14
print(Student.PI) # 3.1
