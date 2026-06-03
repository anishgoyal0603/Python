class Teacher:
    def m1(self):
        print("m1")

class Teacher:
    def m2(self):
        print("m2")

t1 = Teacher()    
#t1.m1()         # AttributeError: 'Teacher' object has no attribute 'm1'   
t1.m2()