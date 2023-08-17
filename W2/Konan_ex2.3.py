import csv

total_salary = 0
num_records = 0
average_age = 0
sum_age = 0

name = [] #creates an empty table (list) named name
age = [] #creates an empty table (list) named age
salary = [] #creates an empty table (list) named salary

with open("example.csv") as csvfiles:
    file = csv.reader(csvfiles)
    for record in file:
        #appends the name to the name array (table)
        name.append(record[0])
        #appends the name to the age array (table)
        age.append(int(record[1]))
        #appends the name to the salary array (table)
        salary.append(int(record[2]))
        num_records = num_records + 1
        
#remember that the range is from 0 to 1 less than num_records
for index in range(0, num_records):
    #adding the salary to total salary. Index is the position in the table
    total_salary = total_salary + salary[index]
    
print("Total salary is $" + str(total_salary))

for index in range(0, num_records):
    sum_age = sum_age + age[index]
    
average_age = sum_age / num_records

print("The average age is " + str(average_age))

        