print "Reverse a word"
word = raw_input("What is your word?: ")
x = ""
for letter in word:
    x = letter+x
print x