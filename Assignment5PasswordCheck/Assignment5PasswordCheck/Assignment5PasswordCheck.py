def passwordCheck():
    password = raw_input("Please input a password: ")
    if len(password) <= 4:
        print "This password is too weak, please try again."
        passwordCheck()
    elif len(password) >= 10:
        print "This password is very strong!"
    elif password.isupper or password.isspace or password.isdigit:
        print "This password is medium"
passwordCheck()