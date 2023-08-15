import time

for x in range (6):
    print (x)

def valX() :
    
    for x in range (10):
        
        print ("***Value of x = " + str(x) +"***" + "\r\n")
        print ("Repetition #:" + str(x) + "\r\n")
        print ("1. Render Graphics" + "\r\n")
        print ("2. Render Audio" + "\r\n")
        print ("3. Execute AI" + "\r\n")
        print ("4. Perform Networking" + "\r\n")
        print ("5. Strobe Keyboard/mouse" + "\r\n")
        
        time.sleep(2)
    
valX()
    
while True :
    
    choice = input("Would you like to contiue? [Y/N]")
    
    if str(choice) == "Y" or str(choice) == "y" :
        valX()
        
    if str(choice) == "N" or str(choice) == "n" :
        
        print("----END OF GAME LOOP----")
        
        break
        
    #Error trap
    while str(choice) != "Y" and str(choice) != "y" and str(choice) != "n" and str(choice) != "N" :
         
         print("INVALID ENTRY!")
         
         choice = input("Would you like to contiue? [Y/N]")
         
         if str(choice) == "Y" or str(choice) == "y" :
            valX()
        
         if str(choice) == "N" or str(choice) == "n" :
        
            print("----END OF GAME LOOP----")
        
            break
         
        
        