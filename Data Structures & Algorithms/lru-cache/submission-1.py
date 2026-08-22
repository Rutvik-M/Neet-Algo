from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Mark as recently used
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If key already exists, move it to MRU position
        if key in self.cache:
            self.cache.move_to_end(key)

        # Add/update the key
        self.cache[key] = value

        # Remove least recently used item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)