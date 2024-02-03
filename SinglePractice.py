class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class EmptyList(Exception):
	pass
class Linked:
	def __init__(self):
		self.head=None
		self.tail =None
		self.length =0

	def __len__(self):
		return self.length
	
	def push(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			c= self.head
			while c.next:
				c=c.next
			c.next = new_node
			self.tail=new_node
		self.length +=1
	def pop(self):
		if self.head is None:
			return EmptyList
		if len(self) == 1:
			deleted =self.head
			self.head =None
			self.length=0
		else:
			c =self.head
			while c.next:
				prev = c
				c = c.next
			deleted=c
			prev.next = None
			self.length -=1
		return deleted 
	
	def unshift(self,value):
		new_node =Node(value)
		new_node.next = self.head
		self.head = new_node
		self.length += 1
	def shift(self):
		if len(self) == 1:
			self.head = None
			self.length =0
		
		c=self.head
		self.head =c.next

	def delete(self,value):
		if len(self)==1:
			self.head = None
			self.length=0
		c= self.head
		while c.next:
			prev = c
			c=c.next
			if c.data == value:
				break
		prev.next = c.next
		self.length -= 1
	def insert(self,value,index):
		c=self.head
		counter=0
		if index==1:
			return self.unshift(value)
		while c.next and counter<index-1:
			prev= c
			c= c.next
			counter+=1
		new_node=Node(value)
		new_node.next = prev.next
		prev.next=new_node
		self.length += 1

	def reverselist(self,head):
		if not head:
			return None
		n_head=head
		if head.next:
			n_head=self.reverselist(head.next)
			head.next.next =head
		head.next=None
		self.head=n_head
		self.tail=head
		return n_head

	def reverse(self):
		prev=None
		c=self.head
		while c:
			next = c.next
			c.next=prev
			prev=c
			c=next
		self.head=prev

	def deletemiddle(self):
		if not self.head:
			return None
		slow=self.head
		fast= self.head
		while fast and fast.next:
			prev=slow
			slow= slow.next
			fast = fast.next.next
		
		print(slow.data)
		prev.next = slow.next

	def getkth(self,head,p,counter=0):
		
		if head:
			if counter==(p-1):
				return head.data
			return self.getkth(head.next,p,counter+1)
		
	def listarr(self):
		arr=[]
		c=self.head
		while c:
			arr.append(c.data)
			c=c.next
		return arr

	def get(self,i):
		c=self.head
		counter=0
		while c.next and counter<(i-1):
			c= c.next
			counter +=1 
		return c

	def power(self):
		self.head=None
		self.tail=None


	def partrev(self,l,r):
		c=self.head
		counter=0
		while c.next and counter<(l-1):
			pre=c
			c=c.next
			counter+=1
		
		prev=None
		for _ in range((r-l)+1):
			n=c.next
			c.next=prev
			prev=c
			c=n
		print(l)
		if l==1:
			self.head=prev
			return

		pre.next.next=c

		pre.next=prev

	def partreverse(self, l, r):
		current = self.head
		counter = 1

		while current and counter < l:
			pre = current
			current = current.next
			counter += 1
		prev = None
		for _ in range((r - l) + 1):
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node

		if counter > 1:
			pre.next.next = current

		if counter == 1:
			self.head = prev
		else:
			pre.next = prev
			
			


	
	def traverse(self):
		current = self.head
		while (current):
			print(current.data, end="->")
			current = current.next


			
l=Linked()
l.push(10)
l.push(20)
l.push(30)

l.traverse()
print("")
l.partrev(1,2)
l.traverse()
print(l.listarr())


