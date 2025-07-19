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

    def popFirst(self):
        if self.head is None:
            return None
        else:
            poped_node = self.head
            self.head = self.head.next
            poped_node.next = None
            self.length-=1
            if self.length == 0:
                self.tail = None
            return poped_node.value



# case 1 
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.print_list()
print(f"popped value -> {ll.popFirst()}")
ll.print_list()

# case 2
ll = LinkedList(10)
ll.print_list()
print(f"popped value -> {ll.popFirst()}")
ll.print_list()

#case3 
ll.print_list()
print(f"popped value -> {ll.popFirst()}")
ll.print_list()