from database import database as databaseObject
from menu import menu, get_name

database = databaseObject()



while True:
    option = menu()

    if option == 1: #Create a record
        database.new(get_name())
    elif option == 2: #Delete a record
        database.delete(get_name())
    elif option == 3: #Find a record
        database.find(get_name())
    elif option == 4: #Print all records
        database.display()




