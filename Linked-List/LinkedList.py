class Node:
    def __init__(self, value):
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
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is  None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            popped_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_value
        else:
            current = self.head
            while current is not None:
                if current.next is None:
                    self.tail = last
                    self.tail.next = None
                    self.length -= 1
                    return current.value
                last = current
                current = current.next
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next #also make head None if only one node exists
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        removed_node  = prev.next
        prev.next = removed_node.next
        removed_node.next = None
        self.length -=1
        return removed_node
    
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
    
my_linked_list = LinkedList(2)

# my_linked_list.append(2)
# my_linked_list.append(3)
# # print(my_linked_list.tail.next)
# my_linked_list.print_list()
# print()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# # my_linked_list.pop()
# my_linked_list.print_list()
# print(my_linked_list.length)
my_linked_list.prepend(1)
my_linked_list.print_list()
print(my_linked_list.length)