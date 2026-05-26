class Student:
    college_name = "ABC college"

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa

stu1 = Student("Rahul",9.2)

print(stu1.name)
print(stu1.college_name)
print(Student.college_name)
print(Student.name) # AttributeError: type object 'Student' has no attribute 'name'