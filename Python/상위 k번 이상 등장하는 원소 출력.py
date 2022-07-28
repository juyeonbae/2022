from heapq import heappush, heappop, heapify
from collections import Counter



def solution(array, K):
    freqs = Counter(array)
    heap = []
    for element, freq in freqs.items():
        heappush(heap, (-freq, element))

    result = []
    for _ in range(K):
        result.append(heappop(heap)[1])

    return result

solution(array = [1,1,1,2,2,3],K=2)
