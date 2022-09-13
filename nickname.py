# Auto detect text files and perform LF normalization
from enum import auto

text=auto
import random

# variables
firstname = input("What is your fist name?")
lastname = input("what is your last name?")



namearray = ["Steel", "Neutron", "Goddamn", "3D Waffle", "Sexual Chocolate", "Sasquatch"]

#               0,         1,       2, 
#user input      1         2          3


# Randopm numbers


# random variables




n = 3
for n in namearray:

 # menu options
     print("MAIN MENU")
     print("1: Change Name")
     print("2: Display a Random Nickname")
     print("3: Display All Nicknames")
     print("4: Add a Nickname")
     print("5: Remove a Nickname")
     print("6: Exit")
     #menu selection
     opchoice = input("Enter selection 1-6: ")
     if  opchoice == "1":
          print("Option 1")
          firstname = input("What is your fist name?")
          lastname = input("what is your last name?")
          print(firstname +" "+ lastname)
     elif opchoice == "2":
          print("option 2")
          randnickname = random.randint(0,len(namearray)-1)
          print(firstname +" "+ namearray[randnickname] +" "+ lastname)
     elif opchoice == "3":
          print("Option 3")
          print("All stored nicknames are: ")
          for i in namearray:
              print(i, end = ' ')
          print("---")
     elif opchoice == "4":
          print("Option 4")
          addname = input("Add a nickname: ")
          namearray.append(addname)
          ## update list
          
          for i in namearray:
              print(i, end = ' ')
          print("---")

          ### update n
          n = 4
     elif opchoice == "5":
          print("Option 5")
          print("select a nickname to remove (1-...")
          
          for i in namearray:
               print(i, end = " ")
          print("---")

          ### Get interger input   
          romname = int(input("Which nickname would you like to revomve")) - 1
          namearray.pop(romname)
          for i in namearray:
               print(i, end = ' ')
          print("---")

         ### update n           
          n = 3
     elif opchoice == "6":
          print("option 6")
          print("Quit")
          n = 0
     print("-------------------------------------------")

          