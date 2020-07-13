class Stack:
    def __init__(self):
        self.storage = []
        self.size = len(self.storage)

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        val = self.storage.pop(-1)
        self.size -= 1
        return val

    def __repr__(self):
        return f'{self.storage}'