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

    # little complex 
    def reverse(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.print_list()
ll.reverse()
ll.print_list()

ll  = LinkedList(10)
ll.reverse()
ll.print_list()
print(ll.head)
print(ll.tail)

ll.head = None
ll.tail = None
ll.length = 0
ll.reverse()
