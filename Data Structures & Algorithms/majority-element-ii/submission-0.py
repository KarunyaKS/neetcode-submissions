class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        ans=[]
        n=len(nums)
        for num in nums:
            d[num]=d.get(num,0)+1
        
        for num in d:
            if d[num]>n//3:
                ans.append(num)
        return ans