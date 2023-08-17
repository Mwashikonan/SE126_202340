import csv

num_record = 0
num_cans = 0
num_party = 0
max_votes = 0
num_state = 0



candidate = []
party = []
state = []


    


with open ("Votes.csv") as csvfile:
    
    file = csv.reader(csvfile)
    
    for record in file:
        
        candidate.append(record[0])
        
        party.append(int(record[1]))
        
        state.append(int(record[2]))
        
        num_record += 1
        

print("The total number of votes: " + int(max_votes))
        
for index in range(len(candidate)):
    
    if candidate[index] > max_votes:
        
        candidate = candidate[index]
        

print(candidate, max_votes)
        
        
        
        

    

    
    
    
    
''' 
    for row in file:
        
        if row[1] == candidate:
            
            votes += 1
            
        elif row[2] == party:
            
            num_party += 1
            
        elif row[3] == state:
            
            num_state += 1
 
 
for            
print("Total number of voters is: " + int(num_record))
'''
            


