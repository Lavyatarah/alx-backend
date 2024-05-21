#!/usr/bin/env python3
"""import Basecaching from base_caching"""

from base_caching import BaseCaching


"""create a class"""

class BasicCache(BaseCaching):
    """Cache Class"""
    def put(self, key, item):
        """Assign the dictionary self.cache_data the item value for the key"""
        if key is None or item is None:
            return
        self.cache_data[key]= item

        
        def get(self, key):
            """return the value in self.cache_data linked to key"""
            if key is None:
            return None
        return self.cache_data.get(key, None)

