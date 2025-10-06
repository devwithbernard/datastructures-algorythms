"""
Queue:

Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket. This way of organizing elements is called FIFO: First In First Out.

Basic operations we can do on a queue are:

Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue.
"""

# Implement queue using Python List

queue = []

# Enqueue : Add a new element to the queue
queue.append("A")
queue.append("B")
queue.append("C")
queue.append("D")

print("Queue:", queue)

# Dequeue: Removes and returns the first (front) element from the queue
element = queue.pop(0)
print("Dequeue:", element)

# Peek: Returns the first element in the queue
element = queue[0]
print("Peek:", element)

# Is_empty: Checks if the queue is empty
is_empty = len(queue) == 0
print("Is empty:", is_empty)

# Size: Finds the number of elements in the queue
size = len(queue)
print("Size:", size)