def check(password):
    has_number = False
    for i in password:
        if i.isdigit():
            has_number = True
    return has_number

password = input("Password: ")
has_number = check(password)
print(has_number)