def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before Function Call")
        result=func(*args,**kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello !! {name}")
    return "123"


print(say_hello("Praveen"))
print("-------------------")
say_hello("Praveen")
