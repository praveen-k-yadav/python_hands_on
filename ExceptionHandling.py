# a= input("Enter the number:")
# print(f"Multiplication table of {a} is:")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {int(a) * i}")
# except Exception as e:
#     print("Invalid input")

# try:
#     num=int(input("Enter a integer:"))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered not an integer")
# except IndexError:
#     print("Not valid index")
# finally:
#     print("I am always executed")


# print("Some line 1")
# print("Some lines 2")

# def func1():
#     try:
#         num=int(input("Enter a integer:"))
#         a=[6,3]
#         print(a[num])
#         return 1
#     except ValueError:
#         print("Number entered not an integer")
#         return 0
#     except IndexError:
#         print("Not valid index")
#         return 0
#     finally:
#         print("I am always executed")

# x= func1()
# print(x)

# a= int(input("Enter value between 5 and 9:"))

# if(a<5 or a>9):
#     raise ValueError("Value not between 5 and 9")

#return from finlly always override the one returned from try or except
# def test():
#     try:
#         return "From Try Block"
#     finally:
#         return "From Return Block"
    
# print(test())

# Creating a custom Exception

class AgeError(Exception):
    pass

def check_age(age):
    if (age<0):
        raise AgeError("Age cannot be negative")
    if(age>150):
        raise AgeError("Age is quite large")
    print(f"Age is: {age}")

try:
    check_age(200)
except AgeError as e:
    print(f"Error: {e}")

try:
    check_age(-6)
except AgeError as e:
    print(f"Error: {e}")


try:
    check_age(20)
except AgeError as e:
    print(f"Error: {e}")