# Implement Linked-List in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

current_node = node1

while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next

print("Null")

# Linked Lists types

"""
1- Single Linked List implementation
"""
class SingleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None

s_node1 = SingleNode(1)
s_node2 = SingleNode(2)
s_node3 = SingleNode(3)
s_node4 = SingleNode(4)
s_node5 = SingleNode(5)

s_node1.next = s_node2
s_node2.next = s_node3
s_node3.next = s_node4
s_node4.next = s_node5

current_s_node = s_node1

while current_s_node:
    print(current_s_node.data, end=" -> ")
    current_s_node = current_s_node.next

print("Null")

# Doubly Linked List Implementation

class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None
        self.next = None

d_node1 = DoubleNode(1)
d_node2 = DoubleNode(2)
d_node3 = DoubleNode(3)
d_node4 = DoubleNode(4)
d_node5 = DoubleNode(5)

d_node1.next = d_node2
d_node2.next = d_node3
d_node3.next = d_node4
d_node4.next = d_node5

d_node2.prev = d_node1
d_node3.prev = d_node2
d_node4.prev = d_node3
d_node5.prev = d_node4

print("\nTraversing forward\n")
current_d_node = d_node1

while current_d_node:
    print(current_d_node.data, end=" -> ")
    current_d_node = current_d_node.next
print("Null")

print("\nTraversing backward\n")
current_d_node = d_node5

while current_d_node:
    print(current_d_node.data, end=" -> ")
    current_d_node = current_d_node.prev
print("Null")

# Circular Linked List
d_node1.next = d_node2
d_node2.next = d_node3
d_node3.next = d_node4
d_node4.next = d_node5
d_node5.next = d_node1

print("\nTraversing forward\n")
current_d_node = d_node1
start_d_node = d_node1
current_d_node = current_d_node.next
while current_d_node != start_d_node:
    print(current_d_node.data, end=" -> ")
    current_d_node = current_d_node.next
print(start_d_node.data)