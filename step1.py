import sys
f = open("textcom.txt", "r")  
context = f.read()

c = {} #dictionary creation 
for i in context:
    c[i] = c.get(i, 0) + 1
f.close()
print(c)
print(c[sys.argv[1]])

