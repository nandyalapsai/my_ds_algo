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

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

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

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index-1)
        removed_node = prev.next
        prev.next = removed_node.next
        removed_node.next = None
        self.length - 1
        return removed_node

    

# case 1 
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.print_list()
print(ll.remove(2).value)
ll.print_list()

# case 2
ll = LinkedList(10)
ll.print_list()
print(ll.remove(0))
ll.print_list()

#case3 
ll = LinkedList(10)
ll.head = None
ll.tail = None
ll.length = 0
ll.print_list()
print(ll.remove(0))
ll.print_list()