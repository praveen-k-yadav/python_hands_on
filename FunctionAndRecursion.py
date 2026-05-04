# def calc_sum(a,b):
#     sum= a+b
#     return sum

# print(calc_sum(2,3))

# def print_hello():
#     print("Hello")

# output= print_hello()
# print(output)

# def calc_prod(a,b=2):
#     return (a*b)

# print(calc_prod(4))

# cities=["delhi","gurgaon","jaipur"]

# def print_cities(list):
#     return list
# print(cities)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
    
# x= factorial(5)
# print(x)

# def func(a,b=10,*args,**kwargs):
#     print(a,b,args,kwargs)

# func(1,2,3,4,x=5)

# def info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# info(name="PK",age=26,city="Mumbai")

square=lambda a,b=10:a+b
print(square(5))