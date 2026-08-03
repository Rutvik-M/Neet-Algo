class MinStack:

    def __init__(self):
        self.stack=[]
        self.gmin=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.gmin[-1] if self.gmin else val)
        self.gmin.append(val)      

    def pop(self) -> None:
        self.stack.pop()
        self.gmin.pop()

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.gmin[-1]
        
