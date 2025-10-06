"""
Linked Lists operations
"""

# Find the lowest and the largest values in a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_list(head: Node):
    current_node = head

    while current_node:
        print(current_node.data, end=' -> ')
        current_node = current_node.next

    print("Null")


def find_lowest_value(head: Node):
    min_val = head.data
    current_node: Node | None = head.next

    while current_node:
        if current_node.data < min_val:
            min_val = current_node.data

        current_node = current_node.next

    return min_val

def find_largest_value(head: Node):
    max_val = head.data
    current_node: Node | None = head.next

    while current_node:
        if current_node.data > max_val:
            max_val = current_node.data

        current_node = current_node.next

    return max_val

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

traverse_list(node1)

print("Lowest value:", find_lowest_value(node1))
print("Largest value:", find_largest_value(node1))