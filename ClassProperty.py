# class Student:
#     college_name="DPS"

#     def __init__(self,name):
#         self.name=name
    
#     @classmethod
#     def change_clg_name(cls,new_name):
#         cls.college_name=new_name

# s1=Student("Praveen")
# s2=Student("Rahul")
# print(s1.college_name)
# print(s2.college_name)

# Student.change_clg_name("IIIT")
# print(s1.college_name)
# print(s2.college_name)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    @property
    def result(self):
        if (self.marks>=40):
            return "Pass"
        else:
            return "Fail"
        
s1=Student("Praveen",45)
print(s1.result)