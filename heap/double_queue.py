import heapq

def solution(operations):
    heap = []
    heap_max = []

    for oper in operations:
        act, num = oper.split(" ")
        if act == "I":
            heapq.heappush(heap, int(num))
        else:
            num = int(num)
            if heap:
                if num == 1:
                    heap_max += heapq.nlargest(1, heap)
                    heap = list(set(heap) - set(heap_max))
                    heapq.heapify(heap)
                else:
                    heapq.heappop(heap)
            else:
                pass
    if heap:
        answer = [max(heap), min(heap)]
    else:
        answer = [0, 0]
    return answer


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

#%%
test = [5,2,5,2,4,7]

heapq.heapify(test)
heapq.nlargest(1, test)