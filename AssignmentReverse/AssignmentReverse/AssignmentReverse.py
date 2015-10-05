word = raw_input("Please input your word: ")
totalLetters = ""
w = len(word)
x = len(word) - 1
c = 0
while c < w:
    letter1 = word[x]
    x = x - 1
    c = c + 1
    totalLetters = totalLetters + letter1
print totalLetters
