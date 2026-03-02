from collections import deque

def fifo(capacity, request_count, requests) -> int:
    '''takes in the capacity of the cache, 
    the number of requests (not used in python), 
    and list of requests.
    Returns cache miss count.
    '''
    fifo = deque()
    cache = set()
    misses = 0

    for request in requests:
        if request in cache:
            # this is a cache hit, do nothing
            continue
        else:
            misses += 1
            # this is a new value
            # is the cache full?
            if len(cache) >= capacity:
                # remove the oldest value
                oldest = fifo.popleft()
                cache.remove(oldest)
            # add the new value
            fifo.append(request)
            cache.add(request)
    
    return misses

