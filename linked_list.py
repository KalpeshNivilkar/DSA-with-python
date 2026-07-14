'''class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1.next.val)'''

'''# singly linked list, append method
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head

            while curr.next is not None:
                curr = curr.next

            curr.next = new_node
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
print(ll.head.val)            # 10
print(ll.head.next.val)       # 20
print(ll.head.next.next) 
        


        '''

# practice
# how create a node 
'''class Node:
    def __init__ (self,val):
        self.val = val
        self.next = None
# singlay linked list 
class singlyLinkedList:
    def __init__ (self):
        self.head = None

    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
ll = singlyLinkedList()

# Append nodes
ll.append(10)
ll.append(20)
ll.append(30)


current = ll.head

while current:
    print(current.val, end="->")
    current = current.next









        

    


'''

# practice 
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class singlyLinkedList:
    def __init__(self):
        self.head = None
# append new node in singly linked list 
    def __init__(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = current
sll = singlyLinkedList()

sll.append(10)
sll.append(20)

current = sll.head
while current:
    print(current.val, end="->")
    current = current.next

