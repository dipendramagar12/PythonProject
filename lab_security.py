def generate_ascii_hash(char1, char2, char3):
    value1 = ord(char1)
    value2 = ord(char2)
    value3 = ord(char3)

    result = value1 * value2 * value3
    return result


def check_strength_level(hash_value):
    if hash_value > 500000:
        return "STRONG HASH"
    return "WEAK HASH"


print("Cyber Security - Security Token")

first = input("Enter first character: ")
second = input("Enter second character: ")
third = input("Enter third character: ")

print("\nASCII Values")
print(first, "=", ord(first))
print(second, "=", ord(second))
print(third, "=", ord(third))

hash_result = generate_ascii_hash(first, second, third)
strength = check_strength_level(hash_result)

print("\nSecurity Readout")
print("Characters:", first, second, third)
print("Hash Value:", hash_result)
print("Strength:", strength)