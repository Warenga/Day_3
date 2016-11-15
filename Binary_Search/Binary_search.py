class BinarySearch(list):
	def __init__(self, list_len, step):
		self.listnum = range(0+step, list_len*step+1, step)
		list.__init__(self, self.listnum)
 		self.length = len(self.listnum)
 	
	def search(self, item):
		first = 0
		last = len(self.listnum) - 1
		found = False
		count = 0

		if item not in self.listnum:
			return {'count': count, 'index' : -1}
		else:
			while first <= last and not found:
				midpoint = (first + last) // 2
				
				if self.listnum[first] == item:
					return {'count': count, 'index' : first}
				elif self.listnum[last] == item:
					return {'count': count, 'index' : last}
				elif self.listnum[midpoint] == item:
					count += 1
					found = True
				else:
					if item < self.listnum[midpoint]:
						count += 1
						last = midpoint - 1
					else:
						count += 1
						first = midpoint + 1
			return {'count': count, 'index' : self.listnum.index(item)}

