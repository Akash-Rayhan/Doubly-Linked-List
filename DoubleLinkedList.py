
class Node:
    """The node class
    """
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class DoubleLinkedList:
    """
        Double linked List class

    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add_node(self, value):
        """_add the node function

        Args:
            value (_int): _will be added value
        """
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
            self.size += 1
        else:
            # adding the new node on the front of self.head
            self.head.prev = node
            # assigning the current head as the next node
            node.next = self.head
            # the inserted node is now the new head
            self.head = node
            self.size += 1
    
    def __delete(self, node):
        #case for head
        if node.prev is None:
            self.head = node.next
            self.head.prev = None
        #case for tail
        elif node.next is None:
            
            self.tail = node.prev
            self.tail.next = None
            
        #case for middle elements
        else:
            
            #when we delete this node the previous node of it will be connected to it's next node
            node.prev.next  = node.next
            # At the same time the next node will be connected to the selected node's previous one 
            node.next.prev = node.prev

    def remove_node(self, value):
        """_remove the node

        Args:
            value (integer): _the value which will be removed
        """
        node = self.head
        while node is not None:
            
            if node.value == value:
                self.__delete(node)   
            node = node.next


    def __str__(self):
        elements = []
        node = self.head
        while node is not None:
            elements.append(node.value)
            node = node.next
        return f"[{','.join(str(element) for element in elements )}]"


my_list = DoubleLinkedList()
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(4)
my_list.add_node(5)
print(my_list)

my_list.remove_node(1)
print(my_list)
