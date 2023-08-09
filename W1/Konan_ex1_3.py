#Function def

def DefaultArg(name, msg = "Hello!"):
    print (name)
    print (msg)

    return #no value returned

#Function called

DefaultArg("Tanya") # No second argument

DefaultArg("Tanya", "Yo!") # With second argument







#Function called

#DefaultArg2("Tanya") # No second argument

#DefaultArg2("Tanya", "Yo!") # With second argument

def DefaultArg2(name, msg = "Hello!"):
    
    print (name)
    print (msg)

    return #no value returned









#Function def

def DefaultArg3 (name, msg = "Hello!", num = 7):
    
    print (name)
    print (msg)
    print (num)
    return 7 #value returned

#Function called

DefaultArg3("Tanya", "Yo!")# With second argument

DefaultArg3("Tanya") # No second argument