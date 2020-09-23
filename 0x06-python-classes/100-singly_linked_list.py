#!/usr/bin/python3
class Node:
    """Defines a node of singly-linked list"""

    def __init__(self, data, next_node=None):
        """Initialize data of a node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data from node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data in node"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get data from next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set data in next_node"""
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly-linked list"""

    def __init__(self):
        """Initialize linked list"""
        self.head = None

    def __str__(self):
        """String version of class"""
        ret_str = ""
        current = self.head
        while current:
            ret_str += str(current.data) + "\n"
            current = current.next_node
        return (ret_str[:-1])

    def sorted_insert(self, value):
        """Function to insert new Node at correct position"""
        new = Node(value)

        if self.head is None:
            self.head = new
            return

        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            """Shift node until value"""
            current = current.next_node
        if current.next_node:
            new.next_node = current.next_node
        current.next_node = new
