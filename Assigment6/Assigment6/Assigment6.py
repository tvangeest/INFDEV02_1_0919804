import sys
print "Make some figures!"
x = "*"
space = " "
w = 1
finished = ""
figure = raw_input("square, triangle, circle or smiley?: ").lower()
if figure == "square":
    squareType = raw_input("What type of square? 1 or 2?: ")
    if squareType == "1":
        width = int(raw_input("How long do you want your figure(width): "))
        height = int(raw_input("How many lines do you want your figure(height): "))
        while w != width:
            x = x + "*"
            w = w + 1
        for z in range(0, height):
            finished = finished + x + "\n"
            z = z + 1
        sys.stdout.write(finished)
    elif squareType == "2":
        width = int(raw_input("How long do you want your figure(width): "))
        height = int(raw_input("How many lines do you want your figure(height): "))
        print x
elif figure == "triangle":
    triangleType = raw_input("What kind of triangle? 1 or 2?: ")
    if triangleType == "1":
        height = int(raw_input("How many lines do you want your figure(height): "))
        for z in range(0, height):
            print x
            x = x + "*"
            z = z + 1
elif figure == "circle":
    print "( )"
elif figure == "smiley":
    print ":)"