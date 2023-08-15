#Function def

def DefaultArg3 (name, msg = "Hello!", num= 7):
    
    print (name)
    print (msg)
    print (num)
    
    return num #value returned

#Function called

DefaultArg3("Tanya", "Yo!")# With second argument

DefaultArg3("Tanya") # No second argument
