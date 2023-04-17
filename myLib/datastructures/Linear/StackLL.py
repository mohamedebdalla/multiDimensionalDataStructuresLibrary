from  mylib.datastructures.Linear.SLL import SLL

class StackLL(SLL):
    def __init__(self, top=None):
        super().__init__(top)
    
    def push(self, node):
        super().InsertHead(node)
    
    def pop(self):
        node = self.head
        self.DeleteHead()
        return node
    
    def peek(self):
        return self.head
    
    def InsertTail(self, node):
        pass
    
    def Insert(self, node, position):
        pass
    
    def SortedInsert(self, node):
        pass
    
    def InsertSorted(self, node):
        pass
    
    def DeleteTail(self):
        pass
    
    def Delete(self, node):
        pass

    def isEmpty(self):
        return self.head is None
    
    def push(self, node):
        super().InsertHead(node)
    
    def pop(self):
        node = self.head
        self.DeleteHead()
        return node.data
    
    def peek(self):
        return self.head.data



