MIN_LENGTH = 8
password = input("Enter your password: ")
while len(password) < MIN_LENGTH:
    print("Password must be at least {} characters long".format(MIN_LENGTH))
    password = input("Enter your password: ")
print('*' * len(password))