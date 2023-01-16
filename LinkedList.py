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

    def CreateList(self, NewData):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        NewNode = Node(NewData)

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.HeadVal is None:
            self.HeadVal = NewNode
            return

        # 5. Else traverse till the last node
        Last = self.HeadVal
        while (Last.NextVal):
            Last = Last.NextVal

        # 6. Change the next of last node
        Last.NextVal = NewNode

    def Display(self):
        if len(List) == 0 :
            print("* The List is empty *")
        else:
            print("* The List contains: ")
            print(List)

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
                Size = int(input("How many nodes you want to create: "))
                for n in range(Size):
                    List.append(input("Enter the element: "))
                self.CreateList(List)
            
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

StartProgram = LinkedList()
StartProgram.Choice()