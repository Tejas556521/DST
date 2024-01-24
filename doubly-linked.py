class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node

    def delete_node(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if not current:
            print(f"Node with value {key} not found.")
            return
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        current = None

    def search_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                print(f"Node with value {key} found.")
                return True
            current = current.next
        print(f"Node with value {key} not found.")
        return False

# Example usage:
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert_at_end(10)
doubly_linked_list.insert_at_end(20)
doubly_linked_list.insert_at_end(30)
doubly_linked_list.insert_at_beginning(5)
doubly_linked_list.insert_after_node(doubly_linked_list.head.next, 15)

print("Doubly Linked List (Forward):")
doubly_linked_list.display_forward()

print("Doubly Linked List (Backward):")
doubly_linked_list.display_backward()

doubly_linked_list.search_node(20)
doubly_linked_list.search_node(25)

doubly_linked_list.delete_node(15)

print("Doubly Linked List (Forward) after deletion:")
doubly_linked_list.display_forward()
