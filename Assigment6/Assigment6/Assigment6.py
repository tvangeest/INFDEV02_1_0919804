print "Make some figures!"
x = "*"
space = " "
w = 1
figure = raw_input("square, triangle, circle or smiley?: ").lower()
if figure == "square":
    width = int(raw_input("How long do you want your figure(width): "))
    height = int(raw_input("How many lines do you want your figure(height): "))
    while w != width:
        x = x + "*"
        w = w + 1
    for z in range(0, height):
        print x
        z = z + 1
elif figure == "triangle":
    height = int(raw_input("How many lines do you want your figure(height): "))
    for z in range(0, height):
        print x
        x = x + "*"
        z = z + 1
elif figure == "circle":
    print "( )"
elif figure == "smiley":
    print ":)"