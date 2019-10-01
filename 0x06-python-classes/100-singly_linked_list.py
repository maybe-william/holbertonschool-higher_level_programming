#!/usr/bin/python3
"""100-singly_linked_list

Define a linked list

"""


class Node:
    """A node in a Linked list

    Represent a Node

    """

    __data = None
    __next_node = None

    def __verify_data(d):
        """verify data function

        Verify data

        Args:
            d: the data

        Raises:
            TypeError

        """

        if type(d) != int:
            raise TypeError("data must be an integer")

    def __verify_next(n):
        """verify next_node function

        Verify the next_node

        Args:
            n: the next_node

        Raises:
            TypeError

        """

        if type(n) != Node and n is not None:
            raise TypeError("next_node must be a Node object")

    def __init__(self, data, next_node=None):
        """init function

        Inits

        Args:
            data: the data
            next_node: the next node

        Raises:
            TypeError

        """

        Node.__verify_data(data)
        Node.__verify_next(next_node)
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data getter

        Get data

        Raises:
            TypeError

        Returns:
            the data

        """

        Node.__verify_data(self.__data)
        return self.__data

    @data.setter
    def data(self, value):
        """data setter

        Set data

        Args:
            value: the value to set

        Raises:
            TypeError

        """

        Node.__verify_data(value)
        self.__data = value

    @property
    def next_node(self):
        """next_node getter

        Get next_node

        Raises:
            TypeError

        Returns:
            the next_node

        """

        Node.__verify_next(self.__next_node)
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter

        Set next_node

        Args:
            value: the next node to set

        Raises:
            TypeError

        """

        Node.__verify_next(value)
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list

    Represent the whole linked list

    """

    __head = None

    def __init__(self):
        """init function

        Inits

        """

        pass

    def __str__(self):
        """str function

        Make a string

        Returns:
            a string representation

        """

        string = ""
        temp = self.__head
        if temp is None:
            string = "\n"
            return string
        while temp is not None:
            string = string + str(temp.data) + "\n"
            temp = temp.next_node
        return string

    def sorted_insert(self, value):
        """sorted_insert function

        Insert into linked list sorted

        Args:
            value: the value to insert

        Raises:
            TypeError

        """

        if self.__head is None or self.__head.data > value:
            x = Node(value, self.__head)
            self.__head = x
            return
        temp = self.__head
        while temp.next_node is not None and temp.next_node.data <= value:
            temp = temp.next_node
        x = Node(value, temp.next_node)
        temp.next_node = x
        return
