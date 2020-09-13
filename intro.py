student = {"name": "Kollathat", "age": 22, "courses": ["Math", "CompSci"]}

# update dictionary
# student["phone"] = "555-5555"
# student["name"] = "Nunnicha"
# student.update({"name": "Nunnicha", "age": 22, "phone": "222-2222"})

# delete dictionary
# del student["age"]
# age = student.pop("age")

"""
print(student)
print(student["name"])
print(student["courses"])
print(student.get("name"))
print(student.get("phone", "Not Found"))
# print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
"""

for key, value in student.items():
    print(key, value)