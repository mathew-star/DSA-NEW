#This is the implementation of singlylinked list
#here we have operation like >push >pop >unshift >shift >delete >Clear duplicates
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class EmptyListError(Exception):
    pass

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        #Push an element to the end of the list."""

        if self.head is None:
            self.head = Node(value)
        else:
            tail = self.get(len(self) - 1)
            tail.next = Node(value)
        self.length += 1

    def pop(self):
        #Remove an element from the end of the list."""
        if self.head is None:
            raise EmptyListError
        if len(self) == 1:
            deleted = self.head
            self.head = None
            self.length = 0
            return deleted
        else:
            nodeBeforeTail = self.get(len(self) - 2)
            deleted = nodeBeforeTail.next
            nodeBeforeTail.next = None
            self.length -= 1
            return deleted
    def unshift(self, value):
        #Add an element to the beginning of the linked list.
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
    def shift(self):
        #Delete an element from the beginning of the list.
        if len(self) == 1:
            self.head = None
            self.length = 0
        else:
            self.head = self.head.next
            self.length -= 1
            
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError
        
        elementBefore = self.get(index - 1)
        newNode = Node(value)
        newNode.next = elementBefore.next
        elementBefore.next = newNode
    
    def delete(self,i):
      #delete element at index 
      current = self.head
      counter=0
      i = i-1
      if len(self) ==1:
        self.head =None
        self.length =0

      if current is not None:
        if counter == i:
          self.head = current.next
          current=None
          self.length -=1

      while current and counter < i:

        prev =current
        current = current.next
        counter +=1
      prev.next = current.next
      return self

    def cleardups(self):
      #clear duplicates from a sorted linked list
      current = self.head
      while current.next is not None:
        if current.data == current.next.data:
          new = current.next.next
          current.next = new
          
        else:
          current = current.next
      return self.head

    def get(self, index):
        #get element at the index
        current = self.head
        counter = 0
        while current and counter < index:
            current = current.next
            counter += 1
        return current
    def __len__(self):
        return self.length

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self
    
    def traverse(self):
        current = self.head
        while (current):
            print(current.value, end="->")
            current = current.next


