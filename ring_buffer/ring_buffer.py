class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0
        self.counter = 0

    def append(self, item):
        if self.size < self.capacity:
            self.storage.append(item)
            self.size += 1
            self.counter += 1
            
        elif self.size == self.capacity:
            self.storage[self.counter % self.capacity] = item
            self.counter += 1

    def get(self):
        return self.storage
