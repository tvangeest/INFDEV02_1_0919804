import sys
print "Make some figures!"
x = ""
full = ""
emptyLine = ""
emptyRows = ""
space = ""
finished = ""
figure = raw_input("square, triangle, circle or smiley?: ").lower()
if figure == "square":
    squareType = raw_input("What type of square? 1 or 2?: ")
    if squareType == "1":
        width = int(raw_input("How long do you want your figure(width): "))
        height = int(raw_input("How many lines do you want your figure(height): "))
        for i in range(0, width):
            x = x + "*"
        for i in range(0, height):
            finished = finished + x + "\n"
        sys.stdout.write(finished)
    elif squareType == "2":
        width = int(raw_input("How long do you want your figure(width): "))
        x = x + "*"
        for i in range(0, width):
            full = full + "*"
        for i in range(1, (width-1)):
            space = space + " "
        emptyLine = ( emptyLine + x + space + x + "\n")
        for i in range(1, (width-1)):
            emptyRows = emptyRows + emptyLine
        finished = (full + "\n" + emptyRows + full + "\n")
        sys.stdout.write(finished)
elif figure == "triangle":
    triangleType = raw_input("What kind of triangle? 1 or 2?: ")
    if triangleType == "1":
        height = int(raw_input("How many lines do you want your figure(height): "))
        for i in range(0, height):
            x = x + "*"
            finished = finished + x +"\n"
        sys.stdout.write(finished)
    elif triangleType == "2":
        height = int(raw_input("How many lines do you want your figure(height): "))
        x = x + "*"
        space = space + " "
        for i in range(0,height):
            sys.stdout.write("\n")
            for j in range(0,i):
                for k in range(0, height-j):
                    sys.stdout.write(space)
                sys.stdout.write(x)
    elif figure == "circle":
        print "( )"
elif figure == "smiley":
    print ":)"