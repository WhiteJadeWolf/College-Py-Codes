""" Write a Python program to create a class representing a queue data structure. 
Include methods for enqueueing and dequeuing elements. """

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue.")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
            return None
        rem = self.queue.pop(0)
        print(f"{rem} removed from the queue.")

    def display(self):
        if not self.queue:
            print("Queue is empty.")
            return
        print("Queue:", " <- ".join(map(str, self.queue)))


q = Queue()
while True:
    choice = int(input("\n1 - Enqueue\n2 - Dequeue\n3 - Display Queue\n4 - Exit\nChoice : "))
    match choice:
        case 1:
            q.enqueue(int(input("Enter number to enqueue : ")))
        case 2:
            q.dequeue()
        case 3:
            q.display()
        case 4:
            break
        case _:
            print("INVALID INPUT - TRY AGAIN.\n")
