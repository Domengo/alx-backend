#!/usr/bin/env python3
"""MRUCache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache class
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.lru = None

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            self.lru = key
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.lru
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))

    def get(self, key):
        """Get an item by key
        """
        if key in self.cache_data:
            self.lru = key
            return self.cache_data[key]
        return None
