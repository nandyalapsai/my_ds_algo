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

    def pop(self):
        temp = self.head
        poped_value = None
        if self.head is None:
            return None
        if self.head == self.tail:
            poped_value = self.head.value
            self.head = None
            self.tail = None
            self.length -=1
            return poped_value
        while temp:
            if temp.next == self.tail:
                poped_value = temp.value
                self.tail = temp
                self.tail.next = None
                self.length -=1
            temp = temp.next
        return poped_value

# case 1 
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.print_list()
print(f"popped value -> {ll.pop()}")
ll.print_list()

# case 2
ll = LinkedList(10)
ll.print_list()
print(f"popped value -> {ll.pop()}")
ll.print_list()

#case3 

print(f"popped value -> {ll.pop()}")
ll.print_list()