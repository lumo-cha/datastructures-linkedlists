"""
    Cha Li
    2016 July 18

    This file is used to test the LinkedList and LinkedNode implementation. Nothing needs
    to be modified in this file.
"""
from linkedlist import LinkedList

def yourtests():
    """ optional: use this function to define your own tests """
    yourlist = LinkedList()
    pass


def main():
    """ don't modify this function. even if you do I have a copy of the original to test with """
    mylist = LinkedList()

    # add some initial nodes
    mylist.append(10)
    mylist.append(20)
    mylist.append(30)
    
    # this should display 10 20 30
    print(mylist)

    # add some nodes to the front
    mylist.prepend(0)
    mylist.prepend(-10)

    # this should display: -10 0 10 20 30
    print(mylist)

    mylist.update(0, -20)  # change -10 to -20
    mylist.insert(2, 5)    # insert 5 between 0 and 10
    mylist.insert(5, 25)   # insert 25 between 20 and 30
    mylist.remove(1)       # remove the 0

    # this should display: -20 5 10 20 25 30
    print(mylist)

    mylist.remove(3)        # removes 20
    mylist.append(40)       # add 40 to the end
    mylist.append(50)       # add 50 to the end
    mylist.update(5, 45)    # update 40 to 45
    mylist.remove(5)        # remove 45
    mylist.update(5, 55)    # update 50 to 55
    mylist.prepend(-30)     # add -30 to the front

    # this should display -30 -20 5 10 25 30 55
    print(mylist)


if __name__ == "__main__":
    main()
    # comment out main and uncomment this to run your own tests
    # yourlist()
