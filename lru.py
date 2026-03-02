class LRUNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict() # key of key, points to node
        self.head = None
        self.tail = None
        self.misses = 0
    def access(self, key):
        # is this a hit?
        if key in self.cache:
            # need to update the position of this node
            node = self.cache[key]
            self.move_to_tail(node)

        # is this a miss?
        else:
            self.misses += 1
            new_node = LRUNode(key)
            # is the cache full?
            if len(self.cache) >= self.capacity:
                # evict the head
                self.remove_head()
            
            # simply add the new node to the tail
            self.add_to_tail(new_node)

    def move_to_tail(self, node):
        if node == self.tail:
            # already at the tail, do nothing
            return
        
        # remove the node from its current position
        if node.prev is not None:
            node.prev.next = node.next
        else:
            # this node is the head
            self.head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev
        
        # add the node to the tail
        node.prev, node.next = None, None
        self.add_to_tail(node)

    def remove_head(self):
        if self.head is None:
            return
        
        node = self.head
        del self.cache[node.key]
        if self.head == self.tail:
            # only one node in the list
            self.head = None
            self.tail = None
        else:
            # more than one node in the list
            self.head = node.next
            self.head.prev = None

    def add_to_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.cache[node.key] = node

def lru(capacity, request_count, requests) -> int:
    '''
    Returns cache miss count.
    '''
    lru_cache = LRU(capacity)
    for request in requests:
        lru_cache.access(request)
    return lru_cache.misses