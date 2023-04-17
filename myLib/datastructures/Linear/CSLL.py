from  mylib.datastructures.Linear.SLL import SLL


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

    def Insert(self, node, pos):
        if pos == 0:
            self.InsertHead(node)
            return node
        elif pos >= self.size:
            self.InsertTail(node)
            return node
        
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
    
    def isSorted(self):
        if self.head is None:
            return True
        
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
    
    def SortedInsert(self, node):
        if self.head is None:
            self.InsertHead(node)
            return

        if node.data < self.head.data:
            self.InsertHead(node)
            return

        if node.data > self.tail.data:
            self.InsertTail(node)
            return

        current = self.head
        while current.next != self.head and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        self.size += 1

