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
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self,index,value):
        # Note here it is > length not >=
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        prev = self.get(index-1)
        new_node = Node(value)
        new_node.next = prev.next
        prev.next = new_node
        self.length+=1
        return True

# case 1 
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.print_list()
print(ll.insert(2,25))
ll.print_list()

# case 2
ll = LinkedList(10)
ll.print_list()
print(ll.insert(1,20))
ll.print_list()

#case3 
ll = LinkedList(10)
ll.head = None
ll.tail = None
ll.length = 0
ll.print_list()
print(ll.insert(0,20))
ll.print_list()