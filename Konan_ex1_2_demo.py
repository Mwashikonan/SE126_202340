import time

for x in range (6):
    print (x)

for x in range (10):
    print ("***Value of x = ***" + str(x) + "\r\n")
    print ("Repetition #:" + str(x) + "\r\n")
    print ("1. Render Graphics" + "\r\n")
    print ("2. Render Audio" + "\r\n")
    print ("3. Execute AI" + "\r\n")
    print ("4. Perform Networking" + "\r\n")
    print ("5. Strobe Keyboard/mouse" + "\r\n")
    
    time.sleep(2)
    
print ("---End of Game Loop---" + "\r\n")