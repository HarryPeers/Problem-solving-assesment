def menu():
    return ask_int("\nPlease enter an option:\n    1) Create a record\n    2) Delete a record\n    3) Find a record\n    4) Print all records\n")

def get_name():
    return input("\nPlease enter a name,\n")

def ask_int(prompt):
    while True:
        try:
            option = int(input(prompt)) #If option is not int, it will error, catch error and handle
        except:
            continue
        else:
            return option
    
