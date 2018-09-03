from sys import argv
# read the WYSS section for how to run this
# script, first, second, third, n = argv
data = argv
print type(data)
script = data[0]
first = data[1]
second = data[2]
third = data[3]

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

if first == '-f':
    print "my name is w2t"
    print data