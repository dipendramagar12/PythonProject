number = int(input("Enter a positive integer with at least 3 digits"))

if number <= 0:
    print("Enter positive number")

elif number < 100:
    print("please Enter a number at least 3 digits.")
else:
    print("decimal", number)
    print("binary", bin(number))
    print("Octal", oct(number))
    print("hexadecimal", hex(number))

    last_digit = number % 10
    print("Last digit:", last_digit)

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")