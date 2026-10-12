students = [
    {"name": "Dipen",
     "marks": {"Math": None, "Science": 90, "English": 78}},
    {"name": "Sandesh",
     "marks": {"Math": 70, "Science": 80, "English": 65}},
    {"name": "yash",
     "marks": {"Math": 92, "Science": None, "English": 95}},
    {"name": "Aanand",
     "marks": {"Math": 50, "Science": 60, "English": 80}},
    {"name": "Ayush",
     "marks": {"Math": 78, "Science": 82, "English": None}}
]


def calculate_total(student):
    total = 0
    
    for subject in ["Math", "Science", "English"]:
        mark = student["marks"].get(subject)
       
        if mark is None:
            print("Note:", subject, "mark is missing, counted as 0")
            mark = 0
        total = total + mark
    return total

def calculate_percentage(total):
    percentage = (total / 300) * 100
    return percentage


name = input("Enter a name : ")

try:
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            found = True

            total = calculate_total(student)
            percentage = calculate_percentage(total)

            print("Student name :", student["name"])
            print("Total marks :", total)
            print("Percentage :", round(percentage, 2))

            break

    if not found:
        raise ValueError("Student does not exist.")

except ValueError as error:
    print("Error:", error)