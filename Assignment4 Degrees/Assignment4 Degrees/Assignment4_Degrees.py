repeat = "yes"
while repeat == "yes":
    f = float(raw_input("What is the temperature in Fahrenheit?: "))
    if (f > -459.67):
        c1 = (f - 32) / 1.8
        c2 = round(c1, 2)
        print "That is " , c2 , " degrees Celcius"
        repeat = "no"
    else:
        print "Invalid number, please try again"

repeat2 = "yes"
while repeat2 == "yes":
    c3 = float(raw_input("What is the temperature in Celcius?: "))
    if c3 > -273.14:
        k1 = c3 + 273.15
        k2 = round(k1, 2)
        print "That is " , k2 , " degrees Kelvin"
        repeat2 = "no"
    else:
        print "Invalid number, please try again"

n = int(raw_input("What is your number?"))
n1 = abs(n)
print n1