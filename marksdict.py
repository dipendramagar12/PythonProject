marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}

for student, mark in marks.items():
    print(student, ":", mark)

total = sum(marks.values())
print("Total marks: ", total)

average = total / len(marks)
print("Average marks: ", average)

highest = max(marks)
print("Highest marks: ", highest)

lowest = min(marks)
print("Lowest marks: ", lowest)

for student, mark in marks.items():
    if mark == highest:
        print("name of student with highest marks: ", student)

