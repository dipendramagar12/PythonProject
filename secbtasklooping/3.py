number = int(input("Enter a number: "))

for i in range(1, 11):
    if i == 3:
        continue
    print(f"{number} x {i} = {number * i}")
