import sys
sys.path.append('/myLib/datastructures/nodes/DNode')

from DNode import DNode

class SLL:
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0
        if head is not None:
            self.size += 1
            node = head
            while node.next is not None:
                node = node.next
            self.tail = node
    
    def InsertHead(self, node):
        node.next = self.head
        self.head = node
        self.size += 1
        if self.tail is None:
            self.tail = node
    
    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def Insert(self, node, position):
        if position < 1 or position > self.size + 1:
            print("Error: Invalid position.")
            return
        if position == 1:
            self.InsertHead(node)
        elif position == self.size + 1:
            self.InsertTail(node)
        else:
            current = self.head
            for i in range(position - 2):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
    
    def SortedInsert(self, node):
        if self.isSorted():
            self.InsertSorted(node)
        else:
            self.Sort()
            self.InsertSorted(node)
    
    def InsertSorted(self, node):
        if self.head is None or node.data < self.head.data:
            self.InsertHead(node)
        elif node.data > self.tail.data:
            self.InsertTail(node)
        else:
            current = self.head
            while current.next is not None and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
    
    def Search(self, node):
        current = self.head
        while current is not None:
            if current.data == node.data:
                return current
            current = current.next
        return None
    
    def DeleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
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
            current.next = None
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
    
    def Sort(self):
        if self.head is None or self.head.next is None:
            return
        new_head = None
        current = self.head
        while current is not None:
            next_node = current.next
            if new_head is None or current.data < new_head.data:
                current.next = new_head
                new_head = current
            else:
                node = new_head
                while node.next is not None and node.next.data < current.data:
                    node = node.next
                current.next = node.next
                node.next = current
            current = next_node
        self.head = new_head
        node = self.head
        while node.next is not None:
            node = node.next
        self.tail = node

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    