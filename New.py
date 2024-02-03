"""
1->2->3->4
4 3 2 1
p=2
remove=i=3from be

p=3 >> r=2
(4-p)+1

p=1
remove=4

remove the nth element from the end
"""
class Node:
    def __init__(self,value) :
        self.value=value
        self.next=None
class Linked:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __len__(self):
        return self.length
    def push(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
            self.length+=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1

    def remove_nth(self,pos):
        pos= (len(self)-pos)+1 #pos=2 r=1
        c=self.head
        counter=1
        while c.next and counter<pos: 
            prev=c
            c=c.next
            counter+=1
        if c.next:
            deleted=c
            prev.next=c.next

        else:
            prev.next=None
        


    def display(self):
        c=self.head
        while c:
            print(c.value, end="->")
            c=c.next



l=Linked()
l.push(10)
l.push(20)
l.push(30)
l.push(40)

l.display()
print("")

l.remove_nth(2)
l.display()