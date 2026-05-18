class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s=sorted(s)
        set_t=sorted(t)
        if set_s == set_t:
            return True
        else:
            return False