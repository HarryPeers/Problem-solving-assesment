**Task - High scores database** 

 Design, code and test a system to store and manage user names and their highest score.  The system must be able to   

∙ create a file   

∙ add data to a file   

∙ locate data in the file by name and their highest score   

∙ delete an item and its associated data from the file   

∙ locate and update a high score for a user   

The system need only cater for 10 items  

 

**Requirements**

 

The program should be able to read and write to a .json flat file database. I'm going to use object-orientated program to make the code very simple and maintainable, and easy to replace code. The program must be able to locate data by their name, and display their high score. Delete an item, locate and update items. After every new record/user is added it should remove the lowest score (if total scores are over 10). It should also check that the entered high scores are integers and not another data type. It should check if the file is present and json formatted, if not it should create the file. 

 

When first started, the user should be prompted with a menu with the option to create, delete, find or display all records. On selection, the program should access the database and complete the function requested by the user. When displaying the records, it should sort all records highest to lowest and display it appropriately, when finding a record it should find all records for the name. When creating a record it should be able to remove the lowest value (if more then 10 records) and create the new record. Finally, it should be able to delete new records by name. 

I used python for this as its an easy to use high level programming language. It is very easily capable of doing the tasks requested and the functions in python are simple to use and maintainable unlike some languages like c#. 
