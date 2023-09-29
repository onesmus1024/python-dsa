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



if __name__ == "__main__":
   
    #use case 

    # 1. reverse a string
    string = "Hello World"
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    print(reversed_string)

