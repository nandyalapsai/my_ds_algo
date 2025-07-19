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

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self,index,value):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True

    def set(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False


# case 1 
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.print_list()
print(ll.set(2,25))
ll.print_list()

# case 2
ll = LinkedList(10)
ll.print_list()
print(ll.set(0,20))
ll.print_list()

#case3 
ll = LinkedList(10)
ll.head = None
ll.tail = None
ll.length = 0
ll.print_list()
print(ll.set(0,20))
ll.print_list()