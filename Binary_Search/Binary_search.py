class BinarySearch(list):
	def __init__(self, list_len, step):
		self.liste = range(0+step, list_len*step+1, step)
		list.__init__(self, self.liste)
 		self.length = len(self.liste)

 	def __repr__(self):
		return repr(range(0, self.list_len, self.step))

	def search(self, item):
		first = 0
		last = len(self.liste)
		found = False
		count = 0

		if item not in self.liste:
			return {'count': count, 'index' : -1}
		else:
			while first <= last and not found:
				midpoint = (first + last) // 2
				if self.liste[midpoint] == item:
					count += 1
					found = True
				else:
					if item < self.liste[midpoint]:
						count += 1
						last = midpoint - 1
					else:
						count += 1
						first = midpoint + 1
			return {'count': count, 'index' : self.liste.index(item)}

ten_to_thousand = BinarySearch(100, 10)
search1 = ten_to_thousand.search(880)
print search1


