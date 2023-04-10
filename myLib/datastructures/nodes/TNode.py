class TNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
        self.balance = 0
    
    def __init__(self, data, balance, parent, left, right):
        self.data = data
        self.balance = balance
        self.parent = parent
        self.left = left
        self.right = right
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_left(self, node):
        self.left = node
    
    def get_left(self):
        return self.left
    
    def set_right(self, node):
        self.right = node
    
    def get_right(self):
        return self.right
    
    def set_parent(self, node):
        self.parent = node
    
    def get_parent(self):
        return self.parent
    
    def set_balance(self, balance):
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def print_node(self):
        print(f"Data: {self.data}, Balance: {self.balance}")
    
    def __str__(self):
        return str(self.data)