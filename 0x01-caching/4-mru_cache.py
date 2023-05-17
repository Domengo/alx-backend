#!/usr/bin/env python3
"""MRUCache"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU Cache class
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.mru_order = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache
        """
        if not key or not item:
            return

        self.cache_data[key] = item
        self.mru_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.mru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.mru_order) > BaseCaching.MAX_ITEMS:
            self.mru_order.popitem(last=False)

        self.mru_order.move_to_end(key, False)

    def get(self, key):
        """Get an item by key
        """
        if key in self.cache_data:
            self.mru_order.move_to_end(key, False)
            return self.cache_data[key]
        return None
