import time

class Node: 
	def __init__(self, key, value): 
		self.key = key 
		self.value = value 
		self.next = None


class HashTable: 
	def __init__(self, capacity): 
		self.capacity = capacity 
		self.size = 0
		self.table = [None] * capacity 

	def _hash(self, key): 
		return hash(key) % self.capacity 

	def insert(self, key, value): 
		index = self._hash(key) 

		if self.table[index] is None: 
			self.table[index] = Node(key, value) 
			self.size += 1
		else: 
			current = self.table[index] 
			while current: 
				if current.key == key: 
					current.value = value 
					return
				current = current.next
			new_node = Node(key, value) 
			new_node.next = self.table[index] 
			self.table[index] = new_node 
			self.size += 1

	def search(self, key): 
		index = self._hash(key) 

		current = self.table[index] 
		while current: 
			if current.key == key: 
				return current.value 
			current = current.next

		raise KeyError(key) 

	def remove(self, key): 
		index = self._hash(key) 

		previous = None
		current = self.table[index] 

		while current: 
			if current.key == key: 
				if previous: 
					previous.next = current.next
				else: 
					self.table[index] = current.next
				self.size -= 1
				return
			previous = current 
			current = current.next

		raise KeyError(key) 

	def __len__(self): 
		return self.size 

	def __contains__(self, key): 
		try: 
			self.search(key) 
			return True
		except KeyError: 
			return False

startSelect = time.time()

if __name__ == '__main__': 

	ht = HashTable(50) 

	ht.insert("Cooking", 3) 
	ht.insert("Hiking", 1) 
	ht.insert("Jogging", 1) 
	ht.insert("Skiing", 2) 
	ht.insert("Baking", 5) 
	ht.insert("Snowboarding", 2)
	ht.insert("IceFishing", 3)
	ht.insert("Volleyball", 5)
	ht.insert("Smoking", 5)
	ht.insert("Bartending", 5)
	ht.insert("Chopping", 30)
	ht.insert("Recipies", 10)
	ht.insert("Jogging", 53) 

	print("Smoking" in ht) 
	print("Luge" in ht) 
	print(ht.search("Chopping"))

	ht.insert("Chopping", 4) 
	print(ht.search("Chopping"))

	ht.remove("Bartending") 
	print(len(ht)) 

endSelect = time.time()
	
print("The time of execution of SelectSort is :",
      (endSelect-startSelect) * 10**3, "ms")
