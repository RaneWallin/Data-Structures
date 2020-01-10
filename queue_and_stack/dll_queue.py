import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.queue = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.queue.add_to_tail(value)
        self.size = self.queue.length

    def dequeue(self):
        val = self.queue.remove_from_head()
        self.size = self.queue.length
        return val

    def len(self):
        return self.size
