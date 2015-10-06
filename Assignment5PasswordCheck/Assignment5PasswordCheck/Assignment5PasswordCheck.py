repeat = "yes"
while repeat == "yes":
    password = raw_input("Please input a password: ")
    if len(password) <= 4:
        print "This password is too weak, please try again."
        repeat = raw_input("Try again?: ")
    elif len(password) >= 15:
        print "This password is very strong!"
    elif password.isupper() or password.isdigit():
        print "This password is very strong!"
    else:
        print "This password is medium strength!"
    repeat = raw_input("Try again?: ")