"""
    <your name>
    <start date>

"""


class LinkedNode:
    _next = None     # the LinkedNode that comes after this node
    _data = None     # the value being stored in this node

    def __init__(self, data):
        """ constructor. create a new LinkedNode that contains the given data. """
        pass

    @property
    def next(self):
        """ return the next node """
        pass

    @next.setter
    def next(self, node):
        """ set the next node to the given node """
        pass

    @property
    def data(self):
        """ return the data stored in this node """
        pass

    @data.setter
    def data(self, value):
        """ set the data stored in this node """
        pass
