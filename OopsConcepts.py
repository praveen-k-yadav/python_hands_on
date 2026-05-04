# class Student:
#     name="Karan"

# s1=Student()
# print(s1)
# print(s1.name)

class Student:
    college_name="DPS"#Class attribute

    def __init__(self,fullname,fullmarks,password):
        self.name=fullname #object attributes
        self.marks=fullmarks
        self.__password=password
        print("Adding new Student to DB")
    def hello(self):
        print("Hello",self.name)
    def get_password(self):
        return self.__password
    def __private_method(self):
        return "Hello!~!!"
    @staticmethod
    def welcome():
        print("Welcome!!!") #This is right way of using staticmethod
    @staticmethod
    def get_school():
        print(Student.college_name)#This is not right way of using staticmethod
#  Static Method never receives self, as it make it look like instance method
#     @staticmethod    
#     def get_school(self):
#         print(self.college_name)


s2=Student("Praveen",26,"abcd")
print(s2.name,s2.marks,s2.college_name)
print(s2)
print(s2.college_name)
# print(s2.__password)
# del s2 
# print(s2)
print(s2.get_password())
print(s2.__private_method())
s2.hello()
Student.welcome()
s2.welcome()
s3=Student("Kiran",28,"efgh")
print(s3.name)