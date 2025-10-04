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