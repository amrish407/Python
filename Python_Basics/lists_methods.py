a = [1,2,3]
b = [4,5,6]

c = a+b
print(c)

s = 'a b c d e f'
z = s.split()       #It will take every space and elements to it this is how split works
print(z)


print("")

#Using Conditionals on list
if a in z:
    print("A is in z")
else:
    print("A is not in z")

for i in z:
    print(i)
    

print("")

#Sorting the list
q=[3,2,7,1,6,9]
q.sort()            #It will sort in ascending order
print(q)  
q.reverse()         #It will sort in descending order
print(q)

print("")


print(q.count(3))   #This will count the number
print(q.index(7))   #This wil give index value of the number we want 
print(len(q))       #This says about the length of the string
print(min(q))       #Minimum number in string
print(max(q))       #Maximum number in string