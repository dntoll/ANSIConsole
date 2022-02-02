

class CircularBuffer:

    def __init__(self, size):
        self.size = size
        self.indexOfLastAdded = 0
        self.array = []

    def add(self, value):
        if len(self.array) < self.size:
            
            self.array.append(value)
            self.indexOfLastAdded = len(self.array) -1
            #print("appended")
            #print("index: " + str(self.indexOfLastAdded))
            #print(self.array)
            return
        
        self.indexOfLastAdded += 1
        #wrap around
        if self.indexOfLastAdded >= self.size : 
            self.indexOfLastAdded = 0

        #print("replaced")
        self.array[self.indexOfLastAdded] = value
    
    def getSize(self):
        return len(self.array)

    def get(self, at):
        virtualIndex = self.indexOfLastAdded - self.getSize() + at + 1 # +1 since index begins with 0
        #0 1 2 3 <- index in array
        #1 2 3 4 <- order of addition
        # 3 - 4 + 0 +1 = 0
        #print("VI1:" + str(virtualIndex) + " " + str(self.indexOfLastAdded))
        

        #0 1 2 3 <- index in array
        #5 2 3 4 <- order of addition
        # 0 - 4 + 0 +1 = -3 (+4 = 1)
        if virtualIndex < 0:
            virtualIndex += self.size

        #print("VI2:" + str(virtualIndex))
        
        return self.array[virtualIndex]

#tests
cb = CircularBuffer(2)
cb.add(1)
assert(cb.getSize() == 1)
assert(cb.get(0) == 1)
cb.add(2)
assert(cb.getSize() == 2)
assert(cb.get(0) == 1)
assert(cb.get(1) == 2)
cb.add(3)
assert(cb.getSize() == 2)
assert(cb.get(0) == 2)
assert(cb.get(1) == 3)
cb.add(4)
assert(cb.getSize() == 2)
assert(cb.get(0) == 3)
assert(cb.get(1) == 4)

