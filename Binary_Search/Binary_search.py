class BinarySearch(list):
	def __init__(self, list_len, step):
		self.liste = range(0+step, list_len*step+1, step)
		list.__init__(self, self.liste)
 		self.length = len(self.liste)

 	def __repr__(self):
		return repr(range(0, self.list_len, self.step))

	def search(self, index):
		first = 0
		last = self.a-1
		found = False
		count = 0
		

		while first <= last and not found:
			midpoint = (first + last) // 2
			if item[midpoint] == item:
				count += 1
				found = True
			else:
				if item < self.item[midpoint]:
					count += 1
					last = midpoint - 1
				else:
					count += 1
					first = midpoint + 1
		return count, found

trial = BinarySearch(20, 2)
print trial[19]

