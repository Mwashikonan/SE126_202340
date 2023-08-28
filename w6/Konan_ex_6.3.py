import csv

nameList = []
ageList = []
phoneList = []
ndx = []

def bubbleSort(nlist):
    for passnum in range(1,len(nlist)):
        for i in range(0,len(nlist)-passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
                

with open ("data.txt") as csvfile:
    file = csv.reader(csvfile)
    for record in file:
        nameList.append(record[0])
        ageList.append(record[1])
        phoneList.append(record[2])
        ndx = ndx + 1
        

bubbleSort(nameList)
print(nameList)

bubbleSort(ageList)
print(ageList)

bubbleSort(phoneList)
print(phoneList)