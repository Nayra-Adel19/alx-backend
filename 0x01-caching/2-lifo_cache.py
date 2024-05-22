#!/usr/bin/python3
""" Create a class LIFOCache that inherits from BaseCaching """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ Create a class LIFOCache that inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self._last_key = None

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data """
        if key is not None and item is not None:
            if (
                len(self.cache_data) == self.MAX_ITEMS
                and key not in self.cache_data.keys()
            ):
                discarded_key = self._last_key
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self._last_key = key

    def get(self, key):
        """ Create a class LIFOCache that inherits from BaseCaching """
        return self.cache_data.get(key, None)
