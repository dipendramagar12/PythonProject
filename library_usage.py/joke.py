import pyjokes
jokes = pyjokes.get_joke()
print("Here is the python jokes")

for i in range(3):
    print(f"joke{i + 1}: ")
print(jokes[i])

answer = input("\n Do you want another joke? (yes/no): ").lower().strip()

while answer == "yes":
    joke = pyjokes.get_joke()
    print("n\ Here is another jokes")
    print(jokes)

    answer = input("\n Do you want another joke? (yes/no): ").lower().strip()

print("Thank you for using the joke generator!")