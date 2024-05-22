#!/usr/bin/python3
""" Must assign to the dictionary self.cache_data """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Must assign to the dictionary self.cache_data """

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Must assign to the dictionary self.cache_data """
        return self.cache_data.get(key, None)
