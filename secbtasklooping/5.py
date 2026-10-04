text = input("Enter a string: ")

seen = []
for char in text:
    if char not in seen:
        seen.append(char)
        count = text.count(char)
        print(f"{char}: {count}")