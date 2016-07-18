"""
    <your name>
    <start date>


"""
from linkednode import LinkedNode


class LinkedList:
    head = None     # the first LinkedNode in the list

    def append(self, value):
        """ add a new LinkedNode, containing the given data, to the tail of the list """
        pass

    def prepend(self, value):
        """ add a new LinkedNode, containing the given data, to the head of the list """

    def update(self, idx, value):
        """ update the data stored in the node at the given index """
        pass

    def insert(self, idx, value):
        """ similar to append but inserting a new LinkedNode with data at the specified index. inserting at 0 means
        the new node will be the first, inserting at 1 means the new node will be the second. Don't forget to relink
        any existing nodes!"""
        pass

    def remove(self, idx):
        """ remove the LinkedNode at the given position. 0 is the first node, 1 is the second node, and so on. Don't
        forget to relink any remaining nodes! """
        pass

    def display(self):
        """ display, in order, the data of every node in the LinkedList. You don't have to do anything with this
        method
        """
        iter = self.head
        while iter is not None:
            print("%s " % iter.data)
            iter = iter.next
