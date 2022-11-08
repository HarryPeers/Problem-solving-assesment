from json import load, dump
from os import getcwd, path
from menu import ask_int
from copy import deepcopy

class database:
    def __init__(self):
        self.cwd = getcwd()
        self.load()

    def create(self):
        #write default file.
        with open(f"{self.cwd}/database.json", "w") as file:
            file.write("{}")
        
    def load(self):
        if not path.exists(f"{self.cwd}/database.json"): #Create file if it doesnt exist
            self.create()
            self.database = {}
        else:
            try:
                with open(f"{self.cwd}/database.json", "r") as file:
                    self.database = load(file) #load file to object attribute
            except: #Json decode error
                self.create()
                self.database = {}

    def save(self):
        #save database to the file.
        with open(f"{self.cwd}/database.json", "w") as file:
            dump(self.database, file, indent=3) 

    def display(self):
        print(f"\nTotal records: {sum([len(self.database[x]) for x in self.database.keys()])}") #get total scores even in sub arrays

        sorted_database = self.sort() #Sort by highscore

        for item in sorted_database:
            print(f"    {item[0]}: {item[1]}") #print all files.
        print("\n\n")

    def sort(self):
        scores = []
        revised = []
        tmp = deepcopy(self.database)
        
        for record in self.database.keys():
            scores += self.database[record] #get all scores in one array

        scores = sorted(scores, reverse=True) #sort array of scores

        for score in scores: #go from highest score to lowest,
            for name in tmp.keys(): # math score with name
                if score in tmp[name]: 
                    revised.append([name, score]) #add to revised scores.
                    tmp[name].remove(score) 
                    break

        return revised
        

    def find(self, name):
        if name not in self.database.keys():
            print("\nRecord not found!\n")
        else:
            print(f"    {name}: {', '.join([str(x) for x in self.database[name]])}") #print all scores for person in one line

    def delete(self, name):
        if name not in self.database.keys():
            print("\nRecord not found!\n")
        else:
            del self.database[name] #delete the key
            self.save()
            print(f"Record deleted!")

    def new(self, name):
        score = ask_int("Please enter a score,\n")
        if sum([len(self.database[x]) for x in self.database.keys()]) == 10:
            lowest = self.sort()[-1]
            if score < lowest[1]:
                print("Your score does not qualify as a top 10")
                return
            else:
                if len(self.database[lowest[0]]) == 1:
                    del self.database[lowest[0]]
                else:
                    self.database[lowest[0]].remove(lowest[1])
        if name in self.database.keys(): #check if name already exists
            self.database[name].append(score) #add to the current score
        else:
            self.database[name] = [score] #create a new name record
        self.save()
        print("\nRecord added\n")
            
        
