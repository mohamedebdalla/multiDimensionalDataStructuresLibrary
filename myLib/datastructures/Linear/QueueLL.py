import sys
sys.path.append('C:/Users/Moe/338_finalProject')
from myLib.datastructures.nodes.DNode import DNode
from .SLL import SLL

class QueueLL(SLL):
    def __init__(self):
        super().__init__()

    def enqueue(self, node):
        self.InsertTail(node)

    def dequeue(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            if self.head is None:
                self.tail = None
            return node

    def front(self):
        if self.head is None:
            return None
        else:
            return self.head

    def rear(self):
        if self.tail is None:
            return None
        else:
            return self.tail

    