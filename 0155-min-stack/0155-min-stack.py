class MinStack:

    def __init__(self):
        self.Minstack=[]

    def push(self, val: int) -> None:
        mn=val if not self.Minstack else min(self.Minstack[-1][1],val)
        self.Minstack.append([val,mn])

    def pop(self) -> None:
        self.Minstack.pop()

    def top(self) -> int:
        return self.Minstack[-1][0]
        

    def getMin(self) -> int:
        return self.Minstack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()