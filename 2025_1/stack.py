class Stack:
    def __init__(self, max_size=100):
        self.data =[]
        self.max_size = max_size
        
    def push(self, value):
        if len(self.data) >= self.max_size:
            print("stack is full")
        else:
            self.data.append(value)
        
    def pop(self):
        if len(self.data) == 0:
            print("stack is empty")
        else:
            return self.data.pop()
        
    
    def is_empty(self):
        return len(self.data) == 0
        
    def is_full(self):
        return len(self.data) == self.max_size
        
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.data)