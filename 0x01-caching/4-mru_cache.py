#!/usr/bin/python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue:
                last = self.queue.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """ Get an item by key """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.mv_last_list(key)
        return item

    def mv_last_list(self, item):
        """ Move an existing item """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)
