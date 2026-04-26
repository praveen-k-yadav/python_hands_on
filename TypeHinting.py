import typing

x:typing.List[str]=["one","two","three"]
print(x)

fees:typing.Dict[str,int]={
    "java":12345,
    "c++":3567436
}
print(fees)

name:str="Praveen"

print(name)

def convertStringToUpperCase(value:str)->str:
    return value.upper()
print(convertStringToUpperCase("abc"))

