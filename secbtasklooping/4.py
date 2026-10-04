number = int(input("Enter a number: "))

reverse = 0
while number > 0:
    digit = number % 10
    reverse = (reverse * 10) + digit
    number //= 10

print("Reverse of the number:", reverse)