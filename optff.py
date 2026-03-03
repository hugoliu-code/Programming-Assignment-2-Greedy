from collections import defaultdict
import heapq
import math
# Evict the element needed farthest in the future

def optff(capacity, requests_count, requests):
    misses = 0

    request_idxs = defaultdict(list)
    for i, r in enumerate(requests):
        request_idxs[r].append(i)

    # Create max heap to keep track of farthest in future
    h = []
    cache = set()

    for r in requests:
        if r in cache:
            continue

        misses += 1
        if len(h) >= capacity:
            i, e = heapq.heappop(h)
            cache.remove(e)
        
        cur_i = request_idxs[r].pop() if len(request_idxs[r]) > 0 else math.inf
        heapq.heappush(h, (-cur_i, r))
        cache.add(r)
    
    return misses
        
            