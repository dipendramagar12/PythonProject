
c_password = "python123"

while True:
    password = input("Enter the password: ")
    if password == c_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password. Try again.")
