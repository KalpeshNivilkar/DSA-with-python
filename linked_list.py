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

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append a node at the end
    def append(self, val):
        new_node = Node(val)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Link the new node
        current.next = new_node

    # Traverse and print the list
    def traverse(self):
        if self.head is None:
            print("The list is empty.")
            return

        current = self.head

        while current is not None:
            print(current.val, end=" -> ")
            current = current.next

        print("None")
# insert at the head and insert at particular position 
    def insert(self,val,position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0

            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            if count != position:
                print("Position out of range")
                return

            new_node.next = current
            prev_node.next = new_node
# delete the head from list 
    def delete_head(self):
        if not self.head:
            print("cant delete the head because the list is empty.")
        else:
            self.head = self.head.next       # The second node (or None) becomes the new head
    
# deleting a node by a value 
    def delete(self,val):
        current = self.head
        if current.val == val:
            self.head = current.next
            return
        else:
            prev_node = None
            found = False

            while current is not None:
                if current.val == val:
                    found = True
                    break
                prev_node = current
                current = current.next
            
            if found:
                prev_node.next = current.next
            else:
                print("Node is not found!")


# Driver Code
sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)

print("Before Deletion:")
sll.traverse()

sll.delete(30)

print("After Deletion:")
sll.traverse()