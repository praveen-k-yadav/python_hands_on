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

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
    
x= factorial(5)
print(x)