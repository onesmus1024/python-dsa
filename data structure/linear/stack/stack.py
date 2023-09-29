class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print("pushed item: " + item)

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()


stack = Stack()
stack.push(str(1))
stack.push(str(2))
stack.push(str(3))
stack.push(str(4))
print("popped item: " + stack.pop())
print("stack after popping an element: " + str(stack.stack))
