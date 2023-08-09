import csv

cont = True

while cont == True:
    eName = input("\n Employee name: ")
    eTitle = input("\n Title: ")
    eMonthHired = input("\n Month Hired: ")
    
    with open ("employee_file_ex4_2.csv", mode='a', newline='') as employee_file:
        
        employee_writer= csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        employee_writer.writerow([eName , eTitle , eMonthHired])
        
        choice = input("\n Do you want to continue?(Y/N): ")
        
        if choice.capitalize() == "N":
            cont == False
            
            print("\n Press any key to contiune ")
        
