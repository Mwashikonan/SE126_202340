#Function def

def DefaultArg (name, msg = "Hello!"):
    print (name)
    print (msg)

    return 7 #no value returned

#Function called

DefaultArg("Tanya") # No second argument

DefaultArg("Tanya", "Yo!")# With second argument