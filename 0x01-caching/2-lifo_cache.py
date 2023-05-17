#!/usr/bin/env python3
"""LIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop()
                del self.cache_data[discard]
                print('DISCARD: {}'.format(discard))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None
