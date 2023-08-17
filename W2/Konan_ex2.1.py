'''
a = 1
b = 2

a,b = b,a #python only

print(a)
print(b)
'''

#Generic approach
a = 1
b = 2

temp = a #A third varible is needed
a = b
b = temp

print(a)
print(b)

