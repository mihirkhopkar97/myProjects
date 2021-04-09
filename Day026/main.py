# list comprehensions

# new_list = [new_item for item in list]

name = 'mihir'
new_list = [item for item in name]
print(new_list)

doubled_list = [item*2 for item in range(1, 5)]
print(doubled_list)

# conditional list comprehension

# new_list = [new_item for item in list if test]

# dictionary comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# conditional dictionary comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)
