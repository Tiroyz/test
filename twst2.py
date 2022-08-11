
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


test = Fifo1()

test.add(10)
print(test.read())
print(test.delete())
print(test.read())

test2 = Fifo1()

test2.add(11)
print(test2.read())