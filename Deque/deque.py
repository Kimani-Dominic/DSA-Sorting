#Enque and Deque operations


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Deque:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None
#Adding elememts in the front
    def enqueue_front(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node
 #Adding elements in the Rear           
    def enqueue_rear(self, element):
        new_node = Node(element)      
        if self.is_empty():
            self.front = self.rear = new_node  
        else:
            self.rear.next = new_node
            self.rear = new_node
#Removing elements from the front            
    def dequeue_front(self):
        if self.is_empty():
            print("Deque is empty")
            return -1
        else:
            removed_element = self.front.data
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next
            return removed_element         
#Removing elements from the rear        
    def dequeue_rear(self):
        if self.is_empty():
            print("Dequeue is empty")         
            return -1
        else:
            removed_element = self.rear.data
            if self.rear == self.front:
                self.rear = self.front = None
            else:
                current = self.front
                while current.next != self.rear:
                    current = current.next
                current.next = None
                self.rear = current
            return removed_element
 #peeking elements in the queue   
    def peek(self):
        if self.is_empty():
            print("No elements")
        else:
            return self.front.data, self.rear.data

# Example Usage
deque = Deque()
deque.enqueue_front(1)
deque.enqueue_front(2)
deque.enqueue_rear(3)

print("Deque after enqueue operations:")
print(deque.peek())  

print("Dequeue operations:")
print(deque.dequeue_front())  
print(deque.dequeue_rear())  

print("Deque after dequeue operations:")
print(deque.peek())  
