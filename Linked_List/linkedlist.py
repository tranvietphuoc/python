


# Singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  # the pointer initially points to nothing

    # traversing value
    def traverse(self):
        node = self  # start from the head node
        while node != None:
            print(node.val)  # access the node value
            node = node.next  # move on to the next node


# Doubly linked list
class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

