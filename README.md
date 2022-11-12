# Doubly-Linked-List
#### A Doubly Linked List (DLL) contains an extra pointer, typically called the previous pointer, together with the next pointer and data which are there in the singly linked list.
#### @ add_node() 
 ##### Add a new Node. 
 ##### The new node is always added before the head of the given Linked List. And newly added node becomes the new head of DLL
 #### @ remove_node(value)
 ##### the passed argument node value will be removed
 
 ### Advantages of DLL over the singly linked list:
 
The delete operation in DLL is more efficient if a pointer to the node to be deleted is given. 

We can quickly insert a new node before a given node. 

In a singly linked list, to delete a node, a pointer to the previous node is needed. To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node using the previous pointer. 

