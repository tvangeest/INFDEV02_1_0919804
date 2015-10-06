import sys
word = raw_input("Input your letters: ")
n = int(raw_input("Input the amount of letters you want to shift: "))

for letter in word:
    letter = ord(letter)
    letter = letter + n
    letter = chr(letter)
    sys.stdout.write(letter) # print without enter
sys.stdout.write("\n")
