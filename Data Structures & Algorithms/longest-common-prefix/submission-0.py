class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs.sort()
        first=strs[0]
        last=strs[len(strs)-1]
        for i in range (len(first)):
            if first[i]==last[i]:
                ans+=first[i]
            else:
                break
        return ans