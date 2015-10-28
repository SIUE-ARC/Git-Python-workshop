__author__ = 'ryanvade'

n = 10
q = 20
v = 0
print("While Loop")
while( v <= n):
    print(v)
    v += 1



letters = ['\n', 'a', 'b', 'c']
numbers = [0,1,2,3]
letterDict = {'a': 0, 'b': 1}
forEach = "For each loop."
print('\n' + forEach)

for k in letterDict:
    print(k, letterDict[k])

for l in letters:
    print(l)

while True:
    if q == 20:
        print(q)
    elif q > n:
        print("q > n")
    elif q <= 0:
        print("Q <= 0")
        break
    pass

    q -= 1

# equivilant to for(int i = 0; i < 4; i++)
for i in range(4):
    print("I = " + str(i))

str1 = "1"
str2 = "2"
int1 = 1
if(str1 == str2):
    print("They are equal")

if(str1 is not int1): #check to see if the two objects are the same(not the value of the two)
    print("Str1 is not int1")

tup = 4, 9, "word", 'c', 4.5, letters, letterDict

print(tup)