from collections import deque

class Fifo1:

    def __init__(self):
        self.a = deque()

    def add(self, val):
        self.a.append(val)
    
    def delete(self):
        return self.a.popleft()
    
class Fifo2():

	def __init__(self):
		self.fifo = list()

	def add(self, val):
		self.fifo.append(val)

	def delete(self):
		return self.fifo.pop(0)

'''В первой реализации используется класс deque, который  реализует двухконечную очередь,
которая поддерживает добавление и удаление элементов с обоих концов в течение О(1) времени.
Во второй реализации используется стандартный список'''
