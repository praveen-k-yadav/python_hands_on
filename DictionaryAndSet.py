# # # dict={
# # #     "name":"Praveen",
# # #     "cgpa":"9.0",
# # #     "marks":[20,35,45],
# # # }
# # # print(dict)
# # # print(type(dict))
# # # print(dict["name"])
# # # dict["name"]="Kiran"
# # # print(dict)

# # # null_dict=()
# # # print(null_dict)

# # student= {
# #     "name":"Rahul",
# #     "score":{
# #         "chem":98,
# #         "phy":99,
# #         "math":100
# #     }
# # }
# # print(student["score"]["chem"])
# # print(student.keys())
# # print(student.items())
# # print(student.values())
# # print(student.get("age"))#it will never give error
# # # print(student["age"])#it will give error
# # # new_dict={"city":"jaipur"}
# # # student.update(new_dict)
# # student.update({"city":"jaipur"})
# # print(student)

# collection={1,2,2,2,"Python","world"}
# print(collection)
# print(type(collection))
# print(len(collection))
# collection.add(13)
# print(collection)
# # collection.pop()
# # print(collection)
# # collection.clear()
# # print(collection)
# collection2= {2,"C"}
# print(collection.union(collection2))
# print(collection.intersection(collection2))
# store={9,"9.0"}
# print(store)
store= {
    ("float",9.0),
    ("int",9)
}
print(store)