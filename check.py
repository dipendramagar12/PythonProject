student = {
    "name": "Hari",
    "age": 19,
    "course": "Python",
    "city": "Lalitpur"
}

key = input("Enter a key: ")

if key in student:
    print(key,"key exists in the dictionery")
else:
    print(key, "key does not exist")