students = {
    101: {
        "name": "Ram",
        "age": 20,
        "course": "Python"
    },
    102: {
        "name": "Sita",
        "age": 21,
        "course": "Java"
    },
    103: {
        "name": "Hari",
        "age": 19,
        "course": "Python"
    }
}

print("All students:")
for student_id, student in students.items():
    print(f"{student_id}: {student}")

print("\nStudent 102:")
print(students[102])

students[103]["course"] = "JavaScript"

students[104] = {
    "name": "Aayush",
    "age": 20,
    "course": "Python"
}

del students[101]

print("\nFinal dictionary:")
print(students)

try:
    student_id = int(input("\nEnter a student ID to view: "))
except ValueError:
    print("Please enter a valid numeric student ID.")
else:
    student = students.get(student_id)
    if student is None:
        print(f"No student found with ID {student_id}.")
    else:
        print(f"Student {student_id}: {student}")
print("student 102: ", students[102])

students[103]["course"] = "java"

students[104] = {
    "name": "Gita",
    "age": 22,
    "course": "C++"
}

print(students)
students.pop(101)



print("final dictionery: ", students)