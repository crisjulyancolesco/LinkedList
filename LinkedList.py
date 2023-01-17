# LINKED LIST 

# List
List = []

# Creating Node class
class Node:
    def __init__(self, DataVal = None):
      self.DataVal = DataVal
      self.NextVal = None

# Creating the LinkedList class
class LinkedList:
    def __init__(self):
      self.HeadVal = None

    # 1. Create List
    def CreateList(self, NewData):

        NewNode = Node(NewData)

        # Checks if the list is empty
        if self.HeadVal is None:
            self.HeadVal = NewNode
            return

        Last = self.HeadVal
        while (Last.NextVal):
            Last = Last.NextVal

        # Makes the last node the new node
        Last.NextVal = NewNode

    # 2. Add at Beginning
    def AddBeginning(self, NewData):
        List.insert(0, NewData) # Add elements at 0 index
        print(List)
    
    # 3. Add After
    def AddAfter(self, NewData, PrevNode):   
        if PrevNode > len(List):
            print("\n  * Position out of range *")
        
        else:
            List.insert(PrevNode, NewData) # add element after the inputted postiion
            print(f"\n List is: {List}")

    # 4. Delete
    def Delete(self):
        El = input("\n Enter the element for deletion: ")
        if El in List:
            List.remove(El) # remove the element
            print(List)
        else:
            print("\n * Element does not exist *")
        
    # 5. Display
    def Display(self):

        # if statements to check if the list is empty or not
        if len(List) == 0 :
            print("\n * The List is empty *")
        else:
            print("\n The List contains: ")
            print(List) # Display the list
    
    # 6. Count
    def Count(self):
        Len = len(List) # count the length of the list
        print(f"\n Number of elements are: {Len}")

    # 7. Reverse
    def Reverse(self):
        List.reverse() # Reverse the list
        print(f"\n The reversed list is:\n{List}")

    # 8. Search
    def Search(self, Key):
        if Key in List:
            Index = List.index(Key) # Determine the index
            print(f"\n Element {Key} found at position {Index}")
        
        else:
            print("\n * Element does not exist *")
    
    # MainMenu where the choices can be found
    def MainMenu(self):
        global UserInput
        print("")
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
                Size = int(input("\n How many nodes you want to create: "))
                for n in range(Size):
                    List.append(input(" Enter the element: "))
                self.CreateList(List)
            
            if UserInput == 2: # Add at Beginning of the list
                El = (input("\n Enter the element: "))
                self.AddBeginning(El)

            if UserInput == 3: # Add After a node in the list
                El = input("\n Enter the element: ")
                Pos = int(input(" Enter the position after which this element is inserted: "))
                self.AddAfter(El, Pos)

            if UserInput == 4: # Delete a node in the list
                if len(List) == 0:
                    print("* The list is empty *")
                else:
                    self.Delete()
            
            if UserInput == 5: # Display the list
                self.Display()

            if UserInput == 6: # Count the nodes in the list
                self.Count()
            
            if UserInput == 7: # Reverse the order of the list
                self.Reverse()

            if UserInput == 8: # Search a node in List
                El = input("\n Enter the element to be searched: ")
                self.Search(El)
            
            if UserInput == 9: # Quit program
                print(" * Thank you for using the LINKED LIST program. *")
                break

StartProgram = LinkedList()
StartProgram.Choice()