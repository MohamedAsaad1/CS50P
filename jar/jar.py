class Jar:
    def __init__(self, capacity=12,):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        n = ""
        for i in range(self.size):
            n += "🍪"
        return f"{n}"

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Capacity the jar is full")

    def withdraw(self, n):
        if n and self.size == 0:
            raise ValueError("Capacity the jar is empty")
        if n > self.size:
            raise ValueError("Capacity the jar is empty")
        self.size -= n



    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity):
        if capacity <= 0 or isinstance(capacity, float):
            raise ValueError("Invalid")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, n):
        self._size = n













