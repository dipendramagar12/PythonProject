student = {
    "name": "Ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
}

print("student information: ", student)

student["marks"] += 5
print(student) 

student["status"] = "pass" if student["marks"] >= 40 else "fail"
print("Update student information: ",student)