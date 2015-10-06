repeat = "yes"
while repeat == "yes":
    password = raw_input("Please input a password: ")
    count = 0
    for letter in password:
        if letter.isupper() or letter.isspace() or letter.isdigit():
            count += 1
    if len(password) <= 4:
        print "This password is too weak, please try again."
    elif len(password) >= 14:
        print "This password is very strong!"
        repeat = "no"
    elif count >= 6:
        print "This password is very strong!"
        repeat = "no"
    else:
        print "This password is medium strength, please try again."