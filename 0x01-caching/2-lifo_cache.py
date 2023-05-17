#!/usr/bin/env python3
"""LIFOCache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
                self.queue.remove(key)
            else:
                del self.cache_data[self.queue[self.MAX_ITEMS - 1]]
                item_discarded = self.queue.pop(self.MAX_ITEMS - 1)
                print("DISCARD:", item_discarded)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None
