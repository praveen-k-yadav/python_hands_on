# class Car:
#     def __init__(self,type):
#         self.type=type

# class Toyota(Car):
#     def __init__(self, type,name):
#         super().__init__(type)
#         self.name=name

# c1=Toyota("Electric","Fortuner")
# print(c1.type)
# print(c1.name)

class A:
    def funcA(self):
        print("Inside A!!")
class B:
    def funcB(self):
        print("Inside B")
class C(A,B):
    def funcC(self):
        print("Inside C!!")

c1=C()
print(c1.funcA())
print(c1.funcB())
print(c1.funcC())

