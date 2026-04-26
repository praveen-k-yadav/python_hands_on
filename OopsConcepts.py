# class Student:
#     name="Karan"

# s1=Student()
# print(s1.name)

class Student:
    college_name="DPS"#Class attribute

    def __init__(self,fullname,fullmarks):
        self.name=fullname #object attributes
        self.marks=fullmarks
        print("Adding new Student to DB")
    def hello(self):
        print("Hello",self.name)
    @staticmethod
    def welcome():
        print("Welcome!!!")

s2=Student("Praveen",26)
print(s2.name,s2.marks,s2.college_name)
s2.hello()
Student.welcome()
s2.welcome()
s3=Student("Kiran",28)
print(s3.name)