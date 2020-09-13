courses = ["History", "Math", "Physics", "CompSci"]

"""
# courses_2 = ["Arts", "Education"]

# courses.append("Arts")
# courses.insert(0, "Arts")
# courses.insert(0, courses_2)
# courses.extend(courses_2)

# courses.remove("Math")
# courses.pop()
# poped = courses.pop()

# print(poped)

nums = [1, 5, 2, 4, 3]

# sort decending
nums.sort(reverse=True)

# sort ascending
nums.sort()

# courses.reverse()
courses.sort(reverse=True)

sorted_courses = sorted(courses)

print(courses)
print(sorted_courses)
print(nums)
print(sum(nums))
print(courses.index("Math"))
print("Arts" in courses)

for item in courses:
    print(item)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = " - ".join(courses)

new_list = course_str.split(" - ")

print(course_str)
print(new_list)
"""

"""
# mutable
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = "Art"

print(list_1)
print(list_2)
"""

"""
# immutable
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = "Art"

print(tuple_1)
print(tuple_2)
"""

"""
# sets
cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
art_courses = {"History", "Math", "Art", "Design"}

print(cs_courses)
print("Math" in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
"""

# empty lists
empty_list = []
empty_list = list()

# empty tuples
empty_tuple = ()
empty_tuple = tuple()

# empty sets
empty_set = {}  # this isn't right! it's a dictionary
empty_set = set()