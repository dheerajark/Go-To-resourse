import math


# 1.Implement a function to reverse a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class Linked_List:
    def __init__(self):
        self.head = None
        
    def last_insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        # if self.head is None:
        #     print("List is empty")
        #     return
        current = self.head
        while current:
            print(current.data, end=" => ")
            current = current.next
        print(None)   
        
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        prev_node = self.head
        
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data   
    
            
list = Linked_List()
list.last_insert(1)
list.last_insert(2)
list.last_insert(3)
list.last_insert(4)
list.last_insert(5)
list.last_insert(6)

result = list.find_middle()
print(result)        
        


