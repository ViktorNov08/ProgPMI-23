class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_position(self, k, data):
        new_node = Node(data)
        if k == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(k - 1):
                if current is None:
                    print("Error: Invalid position")
                    return
                current = current.next
            if current is None:
                print("Error: Invalid position")
                return
            new_node.next = current.next
            current.next = new_node

    def delete_at_position(self, k):
        if self.head is None:
            print("Error: List is empty")
            return

        if k == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(k - 1):
                if current is None:
                    print("Error: Invalid position")
                    return
                current = current.next
            if current is None or current.next is None:
                print("Error: Invalid position")
                return
            current.next = current.next.next

    def multiply_elements(self):
        if self.head is None:
            print("Error: List is empty")
            return

        min_val = self.head.data
        max_val = self.head.data
        current = self.head

        while current:
            if current.data < min_val:
                min_val = current.data
            if current.data > max_val:
                max_val = current.data
            current = current.next

        current = self.head
        while current:
            if min_val < 0:
                current.data *= min_val ** 2
            else:
                current.data *= max_val ** 2
            current = current.next

def main():
    linked_list = LinkedList()

    n = int(input("Enter the number of elements:"))
    for _ in range(n):
        data = float(input("Enter an item: "))
        linked_list.append(data)

    import random
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    for _ in range(n):
        data = random.uniform(a, b)
        linked_list.append(data)

    k = int(input("Enter the position to insert the new element: "))
    data = float(input("Enter a new item:"))
    linked_list.insert_at_position(k, data)

    k = int(input("Enter the position to delete the item: "))
    linked_list.delete_at_position(k)

    linked_list.multiply_elements()

    linked_list.display()

if __name__ == "__main__":
    main()
