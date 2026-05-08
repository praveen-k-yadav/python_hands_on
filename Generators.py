# def count_up_to(n):
#     i=1
#     while(i<=n):
#         yield i
#         i+=1

# gen= count_up_to(5)
# print(next(gen))
# #Each time next(gen) is called, func runs until it hot yield, give back the value and pauses.
# #On the next value it resumes from where it paused
# print(next(gen))

# def count_up_to(n):
#     for i in range(1,n+1):
#         yield i

# for num in count_up_to(5):
#     print(num)

# def generator():
#     yield 1
#     yield 2
#     yield 3
# print(generator())

def normal_func():
    return [1,2,4]

