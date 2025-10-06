"""
Stacks follow This way of organizing elements: LIFO "Last In First Out".
"""

# Implement Stack using Python List

stack = []

# Push: Push at the top
stack.append("A")
stack.append("B")
stack.append("C")

# Pop : Pop the top element
element = stack.pop()
print("Pop:", element)

# Peek : Return the top element
element = stack[-1]
print("Peek:", element)

# isEmpty: Check if the stack is empty
is_empty = len(stack) == 0
print("Is empty:", is_empty)

# Size: Return the size of the stack
size = len(stack)
print("Size:", size)

# Implement Stack using class

class Stack:
    def __init__(self):
        self.stacks = []

    def push(self, element):
        self.stacks.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"

        return self.stacks.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"

        return self.stacks[-1]

    def is_empty(self):
        return len(self.stacks) == 0

    def size(self):
        return len(self.stacks)


# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ", myStack.stacks)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.is_empty())

print("Size: ", myStack.size())