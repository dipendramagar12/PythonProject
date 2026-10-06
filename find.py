numbers = [12, 5, 8, 20, 15, 3, 10]

num = int(input("Enter a number to search: "))

if num in numbers:
    print(f"{num} is exist in the list.")
else:
    print(f"{num} is not exist in the list.")