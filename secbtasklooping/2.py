num = int(input("Enter a number: "))
total = 0
for number in range(1, num + 1):
    if number % 2 != 0:
        total += number

print("Sum of odd numbers:", total)
