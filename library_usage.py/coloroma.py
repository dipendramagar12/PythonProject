from colorama import Fore, Style, init

init(autoreset = True)

print(Fore.GREEN + "Welcome to python!")
print(Fore.RED + "Error: Invalid input!")
print(Fore.YELLOW + "Warning: Please try again.")
print(Fore.CYAN + "Learning python is fun!")

name = input("Enter studnets name: ")
marks = int(input("Enter students marks: "))


print("Student  Result")

print(Fore.CYAN + f"students name : {name}")
print(f"stduents marks: {marks}")

if marks >= 40:
    print(Fore.GREEN + "Result: pass")

else:
    print(Fore.RED + "Result: fail")

print(Style.RESET_ALL + "Thank you!")