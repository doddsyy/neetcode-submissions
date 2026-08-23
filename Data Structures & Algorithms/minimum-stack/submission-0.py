class MinStack:

    def __init__(self):
        self.Stack =[]
        self.MinStack = []

    def push(self, val: int) -> None:
        if self.MinStack:
            if val < self.MinStack[-1]:
                self.MinStack.append(val)
                self.Stack.append(val)
            else:
                self.MinStack.append(self.MinStack[-1])
                self.Stack.append(val)
        else:
            self.Stack.append(val)
            self.MinStack.append(val)

    def pop(self) -> None:
        self.Stack.pop()
        self.MinStack.pop()
        

    def top(self) -> int:
        return self.Stack[-1]
        

    def getMin(self) -> int:     
        return self.MinStack[-1]
        
