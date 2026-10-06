# Q.1
try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    result = n1 / n2
    print("Results: ", result)

except ValueError as e:
    print("Enter a vslid number")

except ZeroDivisionError as e:
    print("Error: cannot divide by zero")

finally:
    print("program exacution completed")


# Q.2
try:
    number = int(input("Enter a number: "))
    square = number * number
    print("square: ",square)
except ValueError as e:
    print("Error: Enter a valid number")
finally:
    print("program execution completed")


# Q.3

number = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter a number"))
    print("value: ", number[index])

except ValueError as e:
    print("Error: Enter a valid number")
except IndexError as e:
    print("Error: index is out of range")
finally:
    print("program execution completed")


# Q.4 list comprehension

square = [ number * number for number in range(1,11)]
print(square)

# Q.5

even_number = [ number for number in range(1,21) if number %2 == 0]
print(even_number)


# Q.6

number = [12, 5, 8, 21, 10, 33, 16, 7]

greater_than_10 = [ number for number in number if number > 10]

print("greather than 10: ", greater_than_10)

odd_number = [ number for number in number if number % 2 != 0]
print("Odd number: ", odd_number)

cubes = [ number ** 3 for number in number]
print("Cubes: ", cubes)


# Generator Objects
# Q.7
def count_numbers():
    for number in range(1, 11):
        yield number


for number in count_numbers():
    print(number)


# Q.8
def even_numbers():
    for number in range(0, 20, 2):
        yield number

    for number in even_numbers():
        print(number)


# Q.9
number_list = [1, 2, 3, 4, 5]

def number_generator():
    for number in range(1, 6):
        yield number

print("List:", number_list)

print("Generator values:")

for number in number_generator():
    print(number)


# Q.10
numbers = []

try:
    for number in range(5):
        num = int(input("Enter a number: "))
        numbers.append(num)

    square = [num * num for num in numbers]
    print("Square:", square)

    def cube_generator():
        for num in numbers:
            yield num ** 3

    print("Cube values:")
    for cube in cube_generator():
        print(cube)

except ValueError as e:
    print("Error: Enter a valid number")

finally:
    print("Program execution completed.")
