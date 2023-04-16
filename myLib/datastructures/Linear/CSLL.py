import sys
sys.path.append('C:/Users/Moe/338_finalProject')
from myLib.datastructures.nodes.DNode import DNode
from .SLL import SLL

class CSLL(SLL):
    def __init__(self, head=None):
        super().__init__(head)
        if head is not None:
            self.tail.next = self.head
    
    def InsertHead(self, node):
        super().InsertHead(node)
        if self.tail is None:
            self.tail = node
        self.tail.next = self.head
    
    def InsertTail(self, node):
        super().InsertTail(node)
        self.tail.next = self.head
    
    def DeleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.tail.next = self.head
        self.size -= 1
    
    def DeleteTail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
        self.size -= 1
    
    def Delete(self, node):
        if self.head is None:
            return
        if node == self.head:
            self.DeleteHead()
        elif node == self.tail:
            self.DeleteTail()
        else:
            current = self.head
            while current is not None and current.next != node:
                current = current.next
            if current is not None:
                current.next = node.next
                self.size -= 1
                if node == self.tail:
                    self.tail = current
        self.tail.next = self.head
