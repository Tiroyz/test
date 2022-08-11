class Fifo1:

    def __init__(self):
        self.a = list([1, 2, 3])

    def add(self, val):
        self.a += [val]
    
    def delete(self):
        val = self.a[0]
        self.a = self.a[1:]
        return val

    def read(self): 
        return self.a
    
class Fifo2():

	def __init__(self, data):
		self.fifo = data

	def add(self, value):
		self.fifo.append(value)

	def read(self):
		return self.fifo[0]

	def delete(self):
		return self.fifo.pop(0)
