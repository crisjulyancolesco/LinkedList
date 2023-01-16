# LINKED LIST 
# Creating Node class
class Node:
    def __init__(self, DataVal = None):
      self.DataVal = DataVal
      self.NextVal = None

# Creating the LinkedList class
class LinkedList:
   def __init__(self):
      self.HeadVal = None

class MainProgram:
    def MainMenu(self):
        global UserInput
        print("***** LINKED LIST *****")
        print("""   1. Create List
   2. Add at Beginning
   3. Add After
   4. Delete
   5. Display
   6. Count
   7. Reverse
   8. Search
   9. Quit""")

        UserInput = int(input("Enter your Choice: "))

    def Choice(self):
        while True:
            self.MainMenu()

            if UserInput == 1: # Create List
                self.CreateList()
            
            if UserInput == 2: # Add at Beginning of the list
                self.AddBeginning()

            if UserInput == 3: # Add After a node in the list
                self.AddAfter()

            if UserInput == 4: # Delete a node in the list
                self.Delete()
            
            if UserInput == 5: # Display the list
                self.Display()

            if UserInput == 6: # Count the nodes in the list
                self.Count()
            
            if UserInput == 7: # Reverse the order of the list
                self.Reverse()

            if UserInput == 8: # Search a node in List
                self.Search()
            
            if UserInput == 9: # Quit program
                break

StartProgram = MainProgram()
StartProgram.Choice()
    