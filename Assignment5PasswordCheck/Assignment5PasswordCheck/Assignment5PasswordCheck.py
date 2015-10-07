repeat = "yes"
print "Password needs to be longer than 4 characters and have at least 6 special characters(numbers, space, uppercase) OR be longer than 14 characters and have at least 1 special character(number, space, uppercase)"
while repeat == "yes":
    password = raw_input("Please input a password: ")
    count = 0
    for letter in password:
        if letter.isupper() or letter.isspace() or letter.isdigit():
            count += 1
    if len(password) <= 4:
        print "This password is too weak, please try again."
    elif len(password) >= 14 and count >= 1:
        print "This password is very strong!"
        repeat = "no"
    elif count >= 6:
        print "This password is very strong!"
        repeat = "no"
    else:
        print "This password is medium strength, please try again."