# Link: https://neetcode.io/problems/is-anagram?list=blind75

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=len(s)
        n=len(t)

        if m!=n:
            return False
        
        hm1={}
        for chr in s:
            if chr not in hm1:
                hm1[chr]=1
            else:
                hm1[chr]+=1
        
        hm2={} 
        for chr in t:
            if chr not in hm2:
                hm2[chr]=1
            else:
                hm2[chr]+=1
        
        for key in hm1:
            if key not in hm2 or hm1[key]!=hm2[key]:
                return False
        
        return True