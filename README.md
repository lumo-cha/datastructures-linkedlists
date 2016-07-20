# Linked Lists
Linked lists are one of the fundamental data structures in computer science, along with arrays. They allow memory to be allocated dynamically as more data is added and
are the foundation for many other linked-type data structure such as [trees](https://en.wikipedia.org/wiki/Tree_(data_structure) and
[graphs](https://en.wikipedia.org/wiki/Graph_(abstract_data_type). The majority of modern data structures are based on "linking" memory together and a lot of algorithm
research is performed in this domain.

In this exercise you'll be writing the core functionality of a linked list. The class and method structure is provided
to you already so your task is to implement every method. Your resulting code should be a working linked list. By the time you finish this exercise you'll be familiar
with the concept behind linked data structures.

**YOU CANNOT USE PYTHON'S BUILT-IN LIST DATA STRUCTURE OR ANY OF ITS METHODS**

## Pre-Requisites
You should be familiar with the following concepts before attempting this assignment:
- Github
- Python fundamentals: if-else, loops, functions, variables
- Object-oriented programming fundamentals: classes, objects, constructors, methods, and instance variables (called properties in Python).

## Assignment
Your assignment is to implement all the methods in the following two classes:

### class LinkedNode
This class represents a single node and the various methods that allow you to
manipulate the node. You'll be implementing:
- `__init__()` - this is the constructor
- `next()` - the setter and getter
- `data()` - the setter and getter


### class LinkedList
This class represents the linked list structure itself and contains the methods to perform various operations on the linked list.
- `append()` - add a new node to the end of the linked list
- `prepend()` - add a new node to the front of the linked list
- `update()` - update the value stored in a node
- `insert()` - insert a new node anywhere in the list
- `remove()` - remove a node from the list


## Testing
You can use `driver.py` to test your implementation. `main()` is predefined and
contains comments about the expected output from your code. If you want to write
custom tests you can modify `yourtests()` or create your own function.

## Hints
It is very useful to draw diagrams of linked lists, nodes and arrows, to understand
what changes you need to make for a specific operation. For example, if you want to
understand how to implement `insert()` then draw a linked list and walk through each
operation that needs to be performed. 
