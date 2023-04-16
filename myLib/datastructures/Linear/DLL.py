import sys
sys.path.append('C:/Users/Moe/338_finalProject')
from myLib.datastructures.nodes.DNode import DNode
from .SLL import SLL

class DLL(SLL):
    class DNode(DNode):
        def __init__(self, data=None, next=None, prev=None):
            super().__init__(data, next)
            self.prev = prev

    def __init__(self, head=None):
        super().__init__(head)
        if head is not None:
            node = head
            while node.next is not None:
                node.next.prev = node
                node = node.next
            self.tail = node

    def InsertHead(self, node):
        super().InsertHead(node)
        if node.next is not None:
            node.next.prev = node

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            super().InsertTail(node)
            node.prev = self.tail
            self.tail.next = node

    def Insert(self, node, position):
        super().Insert(node, position)
        if node.next is not None:
            node.next.prev = node
        if node.prev is not None:
            node.prev.next = node

    def DeleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def DeleteTail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
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
