# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("Car Started....")

# car1= Car()
# car1.start()

class Account:
    def __init__(self,acc_num,acc_pass):
        self.acc_num=acc_num
        self.__acc_pass=acc_pass
    def reset(self):
        print(self.__acc_pass)
        return self.__acc_pass
    def __Welcome(self):
        print("Welcome!!")

acc1= Account("12345","abcde")
print(acc1.acc_num)
print(acc1.reset())
print(acc1.__Welcome())