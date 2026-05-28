class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stor = defaultdict(int)
        for num in nums:
            stor[num] += 1
        
        
        heap = []
        for num in stor.keys():
            heapq.heappush(heap, (stor[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        
        
        #res = []
        #for key, value in stor.items():
        #    res.append([value, key])
        #res.sort()

        #ans = []
        #while len(ans) < k:
        #    ans.append(res.pop()[1])
        #return ans
