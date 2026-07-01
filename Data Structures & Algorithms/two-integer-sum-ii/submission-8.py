class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        lo, hi = 0, n-1
        while lo<hi:
            sum = numbers[lo]+numbers[hi]
            if sum == target:
                return [lo+1, hi+1]
            elif sum < target: 
                lo = lo+1
            else:
                hi= hi-1


        