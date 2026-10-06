student = {
    "name": "Sita",
    "age": 21,
    "course": "Python"
}

student["city"] = "ktm"
student["grade"] = "A"
student["age"] = 22
student["course"] = "Data Science"
print(student)

def vertical(student):
    for key, value in student.items():
        print(f"{key}: {value}")

vertical(student)