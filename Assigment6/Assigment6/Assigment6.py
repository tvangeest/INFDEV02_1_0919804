print "Make some figures!"
x = "*"
space = " "
figure = raw_input("square, triangle, circle or smiley?: ").lower()
amount = raw_input("How long do you want your figure(width): ")
line = raw_input("How many lines do you want your figure(height): ")
if figure == "square":
    print "[]"
elif figure == "triangle":
    print "triangle"
elif figure == "circle":
    print "( )"
elif figure == "smiley":
    print ":)"