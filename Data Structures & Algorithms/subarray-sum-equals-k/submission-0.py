class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        count=0
        cursum=0
        for num in nums:
            cursum+=num
            if cursum-k in prefix:
                count+=prefix[cursum-k]
            prefix[cursum]=prefix.get(cursum,0)+1
        return count
        