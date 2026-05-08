# nums= [10,20,30]
# my_iter=iter(nums)#Gets the iterator object
# print(type(my_iter))
# print(next(my_iter))
# print(next(my_iter))

class CountDown:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if(self.current<=0):
            raise StopIteration
        value= self.current
        self.current-=1
        return value

timer= CountDown(5)

for time in timer:
     print(time)

    


