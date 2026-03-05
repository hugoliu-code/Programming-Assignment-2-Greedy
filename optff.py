from collections import defaultdict
import heapq
import math
# Evict the element needed farthest in the future


def optff(capacity, requests_count, requests):
    # nothing can be stored in cache, all misses
    if capacity == 0:
        return requests_count
    
    misses = 0

    request_idxs = defaultdict(list)
    for i in range(len(requests) - 1,-1,-1):
        r = requests[i]
        request_idxs[r].append(i)


    cache = set()

    for r in requests:
        cur = request_idxs[r].pop()

        if r in cache:
            continue
        
        if len(cache) >= capacity:
            max_ind = max(cache, key = lambda x : request_idxs[x][-1] if len(request_idxs[x]) > 0 else math.inf)
            cache.remove(max_ind)
        
        cache.add(r)
        misses += 1


    '''# Create max heap to keep track of farthest in future
    h = []
    cache = set()

    for r in requests:
        if r in cache:
            request_idxs[r].pop()
            # Actually need to loop through here to update the requested item
            idx = 0
            for i in range(len(h)):
                if h[i][1] == r:
                    
            continue

        misses += 1
        if len(h) >= capacity:
            i, e = heapq.heappop(h)
            cache.remove(e)
        
        cur_i = request_idxs[r].pop() if len(request_idxs[r]) > 0 else math.inf
        heapq.heappush(h, (-cur_i, r))
        cache.add(r)'''
    
    return misses