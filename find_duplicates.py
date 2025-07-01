//Link to problem: https://neetcode.io/problems/duplicate-integer?list=blind75

class Solution:
    def hasDuplicate(self,nums):
        hm={}

        for num in nums:
            if num in hm:
                return True
            
            hm[num]=True

        return False