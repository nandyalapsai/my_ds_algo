class Node {
    int value;
    Node next;
    
    public Node(int value) {
        this.value = value;
        this.next = null;
    }
}

public class LinkedList {
    private Node head;
    private Node tail;
    private int length;
    
    public LinkedList(int value) {
        Node newNode = new Node(value);
        this.head = newNode;
        this.tail = newNode;
        this.length = 1;
    }
    
    public void printList() {
        Node temp = this.head;
        while (temp != null) {
            System.out.println(temp.value);
            temp = temp.next;
        }
    }
    
    public boolean append(int value) {
        Node newNode = new Node(value);
        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return true;
    }
    
    public Node pop() {
        if (this.length == 0) {
            return null;
        }
        Node temp = this.head;
        Node prev = this.head;
        while (temp.next != null) {
            prev = temp;
            temp = temp.next;
        }
        this.tail = prev;
        this.tail.next = null;
        this.length--;
        if (this.length == 0) {
            this.head = null;
            this.tail = null;
        }
        return temp;
    }
    
    public boolean prepend(int value) {
        Node newNode = new Node(value);
        if (this.length == 0) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
        return true;
    }
    
    public Node popFirst() {
        if (this.length == 0) {
            return null;
        }
        Node temp = this.head;
        this.head = this.head.next;
        temp.next = null;
        this.length--;
        if (this.length == 0) {
            this.tail = null;
        }
        return temp;
    }
    
    public Node get(int index) {
        if (index < 0 || index >= this.length) {
            return null;
        }
        Node temp = this.head;
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp;
    }
    
    public boolean setValue(int index, int value) {
        Node temp = this.get(index);
        if (temp != null) {
            temp.value = value;
            return true;
        }
        return false;
    }
    
    public boolean insert(int index, int value) {
        if (index < 0 || index > this.length) {
            return false;
        }
        if (index == 0) {
            return this.prepend(value);
        }
        if (index == this.length) {
            return this.append(value);
        }
        Node newNode = new Node(value);
        Node prev = this.get(index - 1);
        newNode.next = prev.next;
        prev.next = newNode;
        this.length++;
        return true;
    }
    
    public Node remove(int index) {
        if (index < 0 || index >= this.length) {
            return null;
        }
        if (index == 0) {
            return this.popFirst();
        }
        if (index == this.length - 1) {
            return this.pop();
        }
        Node prev = this.get(index - 1);
        Node removedNode = prev.next;
        prev.next = removedNode.next;
        removedNode.next = null;
        this.length--;
        return removedNode;
    }
    
    public void reverse() {
        Node temp = this.head;
        this.head = this.tail;
        this.tail = temp;
        Node after = temp.next;
        Node before = null;
        for (int i = 0; i < this.length; i++) {
            after = temp.next;
            temp.next = before;
            before = temp;
            temp = after;
        }
    }
    
    // Getter methods for testing
    public int getLength() {
        return this.length;
    }
    
    public Node getHead() {
        return this.head;
    }
    
    public Node getTail() {
        return this.tail;
    }
    
    // Main method for testing
    public static void main(String[] args) {
        LinkedList myLinkedList = new LinkedList(2);
        
        myLinkedList.prepend(1);
        myLinkedList.printList();
        System.out.println("Length: " + myLinkedList.getLength());
    }
}
