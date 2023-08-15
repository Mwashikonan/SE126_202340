import csv

def printInstructions():
    print("put all your instruction here")
    print("-----------------------------")
    
def readFile():
    recCtr = 0
    paperMedia = 0
    #print("reading of file will be here")
    with open("inventory.csv") as csvfile:
        file = csv.reader(csvfile)
        for record in file:
            recCtr = recCtr + 1
            if record[0] == "books" :
                paperMedia == paperMedia + 1 
            if record[0] == "magazines" :
                paperMedia == paperMedia + 1
            print("{0:10} {1:10}" .format(record[0], record[1]))
            print("-----------------------------")     
    print("Total rec:", recCtr)
    print("Total paper media: ", paperMedia)
    print("-----------------------------") 
    
while True:
    print("<<< MAIN MENU >>>")
    print(" ")
    print("<1> Instructions")
    print("<2> Read file")
    print("<3> Quit")
    choice = input("Select your choice")
    if int(choice) == 1:
        printInstructions()      
    if int(choice) == 2:
        readFile()      
    if int(choice) == 3:
        break
    
    