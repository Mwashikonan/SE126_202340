#Function def

def DefaultArg (name, msg = "Hello!", num = 7):
    
    print (name)
    print (msg)
    print (num)
    return 7 #value returned

#Function called

DefaultArg("Tanya", "Yo!")# With second argument

DefaultArg("Tanya") # No second argument