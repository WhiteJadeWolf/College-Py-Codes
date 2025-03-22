""" Write a Python program to create a class representing a linked list data structure. 
Include methods for displaying linked list data, inserting and deleting nodes. """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' -> ')
            current = current.next
        print('None')
    
    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            print(f"{data} appended successfully.\n")
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode
        print(f"{data} appended successfully.\n")
    
    def insertAtBeg(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        print(f"{data} inserted at beginning successfully.\n")
    
    def insertAtPos(self, data, pos): # 1 indexing
        newnode = Node(data)
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
            return
        current = self.head
        i = 1
        while(i < pos-1 and current is not None):
            current = current.next
        if current is None:
            print("Position out of bounds")
            newnode = None
            return
        newnode.next = current.next
        current.next = newnode

    def deleteNode(self, data):
        current = self.head
        prev = None
        if current and current.data == data:
            self.head = current.next
            current = None
            print(f"{data} deleted successfully.")
            return
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            print(f"{data} was not present in the linked list.")
            return
        prev.next = current.next
        current = None
        print(f"{data} deleted successfully.")

ll = LinkedList()
while True:
    choice = int(input("\nEnter your choice :--\n1 - Insert At Beginning\n2 - Insert At End\n3 - Insert At Position\n4 - Delete A Node\n5- Display the list\n6 - Exit\nChoice : "))
    match(choice):
        case 1:
            ll.insertAtBeg(int(input("Enter number to be inserted at beginning : ")))
        case 2:
            ll.insertAtEnd(int(input("Enter number to be inserted at end : ")))
        case 3:
            n = int(input("Enter number to be inserted : "))
            p = int(input("Enter position : "))
            ll.insertAtPos(n,p)
        case 4:
            ll.deleteNode(int(input("Enter number to be deleted : ")))
        case 5:
            ll.display()
        case 6:
            break
        case _:
            print("INVALID INPUT - TRY AGAIN.")
