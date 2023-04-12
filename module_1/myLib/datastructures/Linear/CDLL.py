import sys
sys.path.append('/myLib/datastructures/nodes/DNode')

from DNode import DNode
from DLL import DLL

class CDLL(DLL):
    def __init__(self, head=None):
        super().__init__(head)
        if head is not None:
            self.head.prev = self.tail
            self.tail.next = self.head

    def InsertHead(self, node):
        super().InsertHead(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def InsertTail(self, node):
        super().InsertTail(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def DeleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1

    def DeleteTail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size -= 1

    def Delete(self, node):
        if self.head is None:
            return
        if node == self.head:
            self.DeleteHead()
        elif node == self.tail:
            self.DeleteTail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
