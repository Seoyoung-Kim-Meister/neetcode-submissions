class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        lst=[]
        for i in range(n):
            lo, hi = 0, n-1
            while lo < hi:
                if lo == i:
                    lo += 1
                    continue
                if hi == i:
                    hi -= 1
                    continue
                if nums[lo]+nums[hi]==-nums[i]:
                    triplet = [nums[i], nums[lo], nums[hi]]
                    triplet.sort()
                    lst.append(triplet)
                    lo += 1
                    hi -= 1
                elif nums[lo]+nums[hi]<-nums[i]:
                    lo = lo+1
                else:
                    hi = hi-1
        
        seen = set()
        result = []

        for tri in lst:
            t=tuple(tri)
            if t not in seen:
                seen.add(t)
                result.append(tri)
        return result                    
