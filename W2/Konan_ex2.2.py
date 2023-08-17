matrix = ['c' , 'a' , 't']

print(matrix) 

print(matrix[0] + "\n") #print first element

matrix[0] = 'b' #change the value of first row
print(matrix)

#allow mixed data types
matrix[2] = 3.1415 #index 2 value changes
print(matrix)

#navigating an array using for-loop
for data in matrix:
    print(data)
    
#print second and third element
   
print("\n\n\n"+"Second and third element\n\n" + matrix[1])
print(matrix[2])

