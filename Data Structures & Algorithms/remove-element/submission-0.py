class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx=0
        cnt=0
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[idx]=nums[i]
                cnt+=1
                idx+=1
        return cnt
                
            
        
