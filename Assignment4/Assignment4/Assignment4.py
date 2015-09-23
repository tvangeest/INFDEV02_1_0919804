f = float(raw_input("What is the temperature in Fahrenheit"))
zero = -459.67
if (f > zero):
    c1 = (f - 32) / 1.8
    c2 = round(c1, 2)
    print "That is " , c2 , " degrees Celcius"
else:
    print "Invalid number"


c3 = float(raw_input("What is the temperature in Celcius"))
k1 = c3 + 273.15
k2 = round(k1, 2)
print "That is " , k2 , " degrees Kelvin"

n = int(raw_input("What is your number?"))
n1 = abs(n)
print n1