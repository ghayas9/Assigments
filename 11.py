import re
def passwordValidation():
    while True:
        password = input("Please enter a password: ")
        if len(password) < 6:
            print("Your password must be at least 6 characters.")
        elif re.search('[0-9]',password) is None:
            print("Your password must have at least 1 number")
        elif re.search('[A-Z]',password) is None:
            print("Your password must have at least 1 uppercase letter.")
        elif re.search('[a-z]',password) is None:
            print("Your password must have at least 1 uppercase letter.")
        elif re.search("['$', '#', '@', '!', '*']",password) is None:
            print("Your password must have at least 1 special character ($, #, @, !, *)")
        else:
            print("Congratulations! Your password is valid.")
            break
passwordValidation()