import sys
word = raw_input("Input your letters: ")
n = int(raw_input("Input the amount of letters you want to shift: "))
z = 0

for c in word:
    c = ord(c)
    c = c + n
    c = chr(c)
    sys.stdout.write(c) # print without enter
print "" # print empty line
