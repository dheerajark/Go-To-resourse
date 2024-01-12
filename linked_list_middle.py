class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
class Linked_list:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_linked_list(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end= "=>")
            current = current.next
            
    def find_middle(self):
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
        
                
        
linked_list = Linked_list()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_linked_list()
linked_list.find_middle()






