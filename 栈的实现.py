class stacklist:
	def __init__(self):
		self.slist=[]
		self.top=None

	def push(self,x):
		self.slist.append(x)
		self.top=len(self.slist)-1

	def pop(self):
		if len(self.slist)==0:
			return 'stack is empty!'
		temp=self.slist.pop()
		self.top-=1
		return temp
	def isEmpty(self):
		return True if not len(self.slist) else False

	def print_stack(self):
		for i in self.slist:
			print i
		# print self.top

# using stack to realize the queue
class queuelist:
	def __init__(self):
		self.s1=stacklist()
		self.s2=stacklist()

	def enqueue(self,x):
		self.s1.push(x)

	def dequeue(self):
		# if self.s1
		if self.s1.isEmpty():
			return None
		while not self.s1.isEmpty():
			self.s2.push(self.s1.pop())
		temp=self.s2.pop()
		while not self.s2.isEmpty():
			self.s1.push(self.s2.pop())
		return temp
	def print_queue(self):
		self.s1.print_stack()

if __name__=="__main__":
	q1=queuelist()
	q1.enqueue(5)
	q1.enqueue(4)
	q1.enqueue(3)
	q1.dequeue()
	q1.print_queue()


