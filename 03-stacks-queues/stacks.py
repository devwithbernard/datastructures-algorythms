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