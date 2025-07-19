class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1    

    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.value}->", end="")
            temp = temp.next
        print("None") 

    def append(self,value):
        new_node = Node(value)
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length+=1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

# case 1:
print("case 1")
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.print_list()
ll.prepend(40)
ll.print_list()

# case 2:
print("case 2")
ll = LinkedList(10)
ll.head = None
ll.tail = None
ll.print_list()
ll.prepend(10)
ll.print_list()

#case 3
print("case 3")
ll = LinkedList(10)
ll.print_list()
ll.prepend(20)
ll.print_list()

