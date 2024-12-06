class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
      
      #change start
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("top from empty stack")
    # You can implement this class however you like