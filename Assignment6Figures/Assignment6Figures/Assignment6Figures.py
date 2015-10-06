import sys
done = ""
figure = raw_input("square1, square2, triangle1, triangle2?: ").lower()
if figure == "square1":
    length = int(raw_input("What is the length of the square?: "))
    width = int(raw_input("What is the width of the square?: "))
    for i in range(width):
        for j in range(length):
            done += "*"
        done += "\n"
    sys.stdout.write(done)
elif figure == "square2":
    length = int(raw_input("What is the length of the square?: "))
    width = length
    for i in range(width):
        done += "*"
    done += "\n"
    for j in range(width-2):
        done += "*"
        for k in range(width-2):    
            done += " "
        done += "*\n"
    for l in range(width):
        done += "*"
    sys.stdout.write(done + "\n")
elif figure == "triangle1":
    length = int(raw_input("What is the length of the triangle?: "))
    for i in range(length):
        for j in range(i+1):
            done += "*"
        done += "\n"
    sys.stdout.write(done)
elif figure == "triangle2":
    length = int(raw_input("What is the length of the triangle?: "))
    for i in range(length):
        for j in range(length, i+1, -1):
            done += " "
        for k in range(i+1):
            done += "*"
        for l in range(i):
            done += "*"
        done += "\n"
    sys.stdout.write(done)

