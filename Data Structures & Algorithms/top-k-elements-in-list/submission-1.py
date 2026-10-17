class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        s=sorted(d,key=d.get,reverse=True)
        return s[:k]
        