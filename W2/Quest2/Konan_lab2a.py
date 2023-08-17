import csv

num_records = 0
roomsOver = 0
over = 0

Rooms = []
Max = []
Min = []

with open ("lab2a.csv") as csvfiles:
    
    file = csv.reader(csvfiles)
    
    for record in file:
        
        Rooms.append(record[0])
        
        Max.append (int(record[1]))
        
        Min.append (int(record[2]))
