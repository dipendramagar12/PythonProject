fruits = [
    "apple", "banana", "apple",
    "orange", "banana", "apple",
    "mango", "orange", "banana"
]
for fruit in set(fruits):
    print(f"{fruit}:", fruits.count(fruit))
    
