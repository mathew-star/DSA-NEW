#This is doubly linked list
class Node:
  def __init__(self,value):
    self.value = value
    self.next =None
    self.prev = None
    
class EmptyList(Exception):
  pass

class Doubly:
  def __init__(self):
    self.head = None
    self.tail = None
    self.len = 0
  def push(self,value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      self.len +=1
    else:
       self.tail.next = new_node
       new_node.prev = self.tail
       self.tail = new_node
  def pop(self):
    poped = self.tail
    self.tail = poped.prev
    self.tail.next = None
    poped.prev = None

  def unshift(self,value):
    n_node= Node(value)
    if self.head is None:
      self.head = n_node
      self.tail = n_node
    else:
      n_node.next = self.head
      self.head.prev = n_node
      self.head = n_node

  def shift(self):
    if self.head is None:
      raise EmptyList
    else:
      shifted = self.head
      self.head =self.head.next
      self.head.prev = None 
      shifted.next =None


  def insert(self,value,p):
    c=self.head
    co=1
    while c.next and co<p:
      c=c.next
      co+=1

    new=Node(value)
    new.next=c
    new.prev=c.prev
    c.prev.next=new






  def display(self):
    c = self.head
    while c:
      print(c.value, end="<-->")
      c = c.next


d=Doubly()
d.push(10)
d.push(20)
d.push(30)


d.insert(9,2)
d.display()