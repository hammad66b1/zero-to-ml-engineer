print("Create Account")

username = input("Enter a username: ")

while len(username) < 6:
    print("Username must be 6 characters or longer")
    username = input("Enter again: ")

password = input("Set a new password: ")

while (
    password.count("0") +
    password.count("1") +
    password.count("2") +
    password.count("3") +
    password.count("4") +
    password.count("5") +
    password.count("6") +
    password.count("7") +
    password.count("8") +
    password.count("9")
) == 0:
    print("Password must contain at least one number")
    password = input("Enter again: ")

print("Account created")
print("Login now:")

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Login failed")